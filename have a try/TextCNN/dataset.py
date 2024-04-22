import warnings

import torch
import numpy as np

from gensim import models
from torch.utils.data import dataset
from torchvision.transforms import ToTensor

UNKNOW_WORD = '<pad>'

class MyDataset(dataset.Dataset):
    def __init__(self,
                  file_path,
                  positive,
                  word_size):
        # 加载单词表文件
        with open(file_path, 'r', encoding='utf-8') as f:
            self.lines = f.readlines()

        self.positive = positive # 正面情感还是负面情感
        self.word_size = word_size # 词向量维度
        # 加载已经训练的word2vec模型
        self.model = models.Word2Vec.load('word2vec.model')

        # 增加一个未知词向量，用来处理之后的未知词
        unknow_vecotr = np.zeros(len(self.model.wv.vectors[0]))
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore",category=UserWarning)
            self.model.wv.add_vectors(UNKNOW_WORD, unknow_vecotr)

    def __len__(self):
        return len(self.lines)

    def __getitem__(self, index):

        words_size = self.word_size
        line = self.lines[index].strip()
        words = line.split(' ')

        # 截取固定长度
        if words_size < len(words):
            words = words[-words_size:]
            # mid = int(len(words) / 2)
            # left = int(mid - words_size / 2)
            # right = int(mid + words_size / 2)
            # words = words[left:right]

        while len(words) < words_size:
            words.append(UNKNOW_WORD)

        # 微调，防意外
        while len(words) > words_size:
            words.pop()

        if self.positive:
            emotions_t = torch.tensor([1.0,0.0])
        else:
            emotions_t = torch.tensor([0.0,1.0])

        DEFAULT_PAD_INDEX = self.model.wv.get_index(UNKNOW_WORD)

        words_indexs = [
            self.model.wv.get_index(word,default=DEFAULT_PAD_INDEX)
                    for word in words]

        #列表转numpy再转tensor
        words_np = np.array(words_indexs)
        words_t = torch.from_numpy(words_np).to(torch.int64)

        return words_t,emotions_t
