import torch
import numpy

a_t = torch.ones(3, 4)
a_np = a_t.numpy()

print(a_np)
a_np[0, 0] = 2
print(a_np)
print(a_t)#a_np和a_t共享内存，修改a_np也会影响a_t
b_np = numpy.ones((2, 3))
b_t = torch.from_numpy(b_np)
print(b_np.dtype)#numpy默认64位浮点数
print(b_t.dtype)#转torch后仍然是64位浮点数，pytorch一般用32位浮点数，最好是转换一下
b_t = b_t.float()
print(b_t.dtype)#转换为32位浮点数

with open('data.t','wb') as f:
    torch.save(a_t, f)

with open('data.t','rb') as f:
    a_t = torch.load(f)
print(a_t)
