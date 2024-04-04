import torch
import numpy as np
import h5py

a_t = torch.ones(3, 4)

with h5py.File('test.h5', 'w') as f:
    f.create_dataset('a_np', data=a_t.numpy()) # a_np 是保存a_t的键，可以使用其他键甚至嵌套键

with h5py.File('test.h5', 'r') as f:
    a_np = f['a_np'][2][1] # 读取a_np的值(这里f['a_np']已经是numpy数组了)
    print(type(a_np))
    if not isinstance(a_np, np.ndarray): # 判断是否是numpy数组.(上一步如果只从f中取出了一个数，
        # 那么a_np会是一个标量，需要判断并转换为numpy数组)
        a_np = np.array(a_np)
    a_t = torch.from_numpy(a_np) # 转换为torch张量
    print(a_t)
