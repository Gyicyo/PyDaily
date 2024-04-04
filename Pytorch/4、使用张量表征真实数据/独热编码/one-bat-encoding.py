import torch

a = torch.randint(0,5,size=(5,))# 加，表明是个元组
a_one = torch.zeros(a.shape[0],5) # 参数：为a中的每一个数进行独热编码，数的总个数（5个不同的数）
a_one.scatter_(1,a.unsqueeze(1),1.0) # 参数：对a_one的1维度操作，将a中的数值作为索引，将1.0赋值到对应位置
print(a.unsqueeze(1))
print(a_one)
