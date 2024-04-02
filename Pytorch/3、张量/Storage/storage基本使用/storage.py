#pylint: disable=E0401
import torch

a = torch.tensor([[1,2], [2,3], [3,4]])

print()
second = a[2]
print(second.storage_offset()) # 偏移量
print(second.stride()) # 步长
print(second.size()) # 大小

# 转置(维度（形状）翻转，步长跟着翻转)
a_t = a.t()
print(a_t.storage_offset()) # 偏移量
print(a_t.stride()) # 步长
print(a_t.shape) # 大小

# 高维转置
b = torch.ones(3,4,5)
b_t_13 = b.transpose(0,2)
print(b.stride(), b_t_13.stride()) # 步长
print(b.shape,b_t_13.shape) # 大小
print(b.storage_offset(), b_t_13.storage_offset()) # 偏移量
