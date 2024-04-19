# 数字预测
import torch
from torchvision.datasets import MNIST
from torchvision import transforms
from torch.utils.data import DataLoader
from torch import nn
import torch.nn.functional as F
from PIL import Image
import matplotlib.pyplot as plt
import h5py

# 定义网络结构
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 10)

    def forward(self, x):
        x = x.view(-1, 784)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

def get_loader(is_train):
    pr = transforms.Compose([transforms.ToTensor()])
    dataset = MNIST(root='../data',train=is_train,transform=pr,target_transform=None,download=True)
    return DataLoader(dataset=dataset, batch_size=15, shuffle=True)

# 训练网络
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = Net().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
train_loader = get_loader(True)
test_loader = get_loader(False)

def train():
    model.train()
    for data, target in train_loader:
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()


def test():
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += criterion(output, target).item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


if __name__ == '__main__':
    for epoch in range(1, 3):
        train()
        test()

    for i, (data, target) in enumerate(train_loader):
        if i>3:
            break
        data = data.to(device)
        pred = torch.argmax(model(data[14].view(-1, 28, 28)))
        data = data.cpu()
        plt.imshow(data[14].view(28, 28), cmap='gray')
        plt.title('pred: {}'.format(pred.item()))
        plt.show()

    torch.save({
        'model':model.state_dict(),
    }, 'number.pth')