import torch

a = torch.tensor(list(range(9)))
# print(a.size()) # 大小
# print(a.storage_offset()) # 偏移量
# print(a.stride()) # 步长

b = a.view(3, 3) # 改变形状(存储区不变)
a[0] = 10
print(b) # b跟着变

c = b[1:,1:] # 切片(存储区不变)
print(c.size()) # (2,2)
print(c.storage_offset()) # 4(这里c已经不是完整的了，最小值为4，偏移量是4)
print(c.stride()) #(3,1)
