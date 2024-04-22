import warnings

import torch
import numpy as np
import torch.nn as nn
import torchvision.transforms as transforms
import torch.nn.functional as F

from torch.utils.data import DataLoader,ConcatDataset
from torch import Tensor
from torch.optim import Adam
from dataset import MyDataset
from gensim.models import word2vec

UNKNOW_WORD = '<pad>'

def get_loader(pos_path, neg_path, batch_size=32, shuffle=True,workers=2,word_size=200):
    pos_dataset = MyDataset(pos_path,positive=True,word_size=word_size)
    neg_dataset = MyDataset(neg_path,positive=False,word_size=word_size)
    dataset = ConcatDataset([pos_dataset,neg_dataset])
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle,num_workers=workers)
    return loader

class TextCNN(nn.Module):
    def __init__(self, vectors_size, words_size, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.words_size = words_size
        self.vectors_size = vectors_size
        word2 = word2vec.Word2Vec.load('word2vec.model')
        unknow_vecotr = np.zeros(len(word2.wv.vectors[0]))

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore",category=UserWarning)
            word2.wv.add_vectors(UNKNOW_WORD, unknow_vecotr)
        self.embedding = nn.Embedding(num_embeddings=word2.wv.vectors.shape[0],
                                     embedding_dim=vectors_size)

        self.embedding.weight.data.copy_(
                        torch.from_numpy(
                        word2.wv.vectors))
        print(f"Embedding shape:{self.embedding.weight.shape}")
        # 卷积层
        self.convs = nn.ModuleList()
        kernel_sizes = [2,3,4]
        num_filters = [256,256,256]
        for kernel_size, num_filter in zip(kernel_sizes, num_filters):
            conv = nn.Sequential(
                nn.Conv1d(in_channels=words_size,
                           out_channels=num_filter,
                             kernel_size=kernel_size,
                               padding='same'),
                nn.PReLU(),
                             )
            self.convs.append(conv)

        self.pool = nn.MaxPool1d(kernel_size=3)
        self.droupout = nn.Dropout(p=0.2)
        # 全连接层
        self.fc1 = nn.Linear(in_features=sum(num_filters)*int(vectors_size/3), out_features=2)

    def forward(self,x):
        x = self.embedding(x)
        # 卷积层
        conv_outputs = []
        for conv in self.convs:
            conv_output = conv(x)
            conv_output = self.pool(conv_output)
            conv_outputs.append(conv_output)

        x = torch.cat(conv_outputs, dim=1)

        x = self.droupout(x)
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = F.softmax(x,dim=1)
        return x

    def save(self,path):
        torch.save(self.state_dict(),path)

def train(epochs,model, train_loader, loss_fn, optimizer, device):
    model.to(device)
    model.train()

    for epoch in range(1,epochs+1):
        for i, (data, label) in enumerate(train_loader):
            data,label = data.to(device),label.to(device)
            # 训练模型
            output = model(data)
            loss = loss_fn(output, label)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if i % 100 == 0:
                print(f"Epoch: {epoch}, step: {i}, loss: {loss.item()}")

def test(model, test_loader, device, is_train):
    model.to(device)
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for i,(data, label) in enumerate(test_loader):
            data,label = data.to(device),label.to(device)
            output = model(data)
            pred = output.argmax(dim=1, keepdim=True)
            label = label.argmax(dim=1, keepdim=True)
            correct += pred.eq(label.view_as(pred)).sum().item()
            total += data.shape[0]

    if is_train:
        print(f"Train Accuracy: {correct/total}")
    else:
        print(f"Test Accuracy: {correct/total}")

def main():
    WORD_SIZE = 200
    VECTORS_SIZE = 300
    BATCH_SIZE = 32
    EPOCHS = 2


    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    loss_fn = nn.CrossEntropyLoss().to(device)
    Textmodel = TextCNN(words_size=WORD_SIZE,
                        vectors_size=VECTORS_SIZE)
    optimizer = Adam(Textmodel.parameters(), lr=3e-4,weight_decay=1e-4)

    train_loader = get_loader('train_pos.csv', 'train_neg.csv',
                              word_size=WORD_SIZE,batch_size=BATCH_SIZE)
    train(
        epochs=EPOCHS,
        model=Textmodel,
        train_loader=train_loader,
        loss_fn=loss_fn,
        optimizer=optimizer,
        device=device
    )

    test_loader = get_loader('test_pos.csv', 'test_neg.csv',
                             word_size=WORD_SIZE,batch_size=BATCH_SIZE)
    test(Textmodel,train_loader,device,is_train=True)
    test(Textmodel,test_loader,device,is_train=False)

    Textmodel.save('TextCNN.pth')

if __name__ == '__main__':
    main()
