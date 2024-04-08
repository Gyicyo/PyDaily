import torch
from torch import Tensor
import torch.optim as optim
from matplotlib import pyplot as plt
#pylint:disable=W0621
t_c = [0.5,14.0,15.0,28.0,11.0,8.0,3.0,-4.0,6.0,13.0,21.0]
t_u = [35.7,55.9,58.2,81.9,56.3,48.9,33.9,21.8,48.4,60.4,68.4]
t_c = torch.tensor(t_c)
t_u = torch.tensor(t_u)

# print((t_u*t_u).mean())
def model(t_u,w,b) -> Tensor: # 输入张量、权重参数、偏置参数
    return w*t_u + b # 输出预测值

def loss_fn(t_p,t_c):
    squared_diffs = (t_p - t_c)**2
    return squared_diffs.mean()

# w = torch.ones(())
# b = torch.zeros(())
# t_p = model(t_u,w,b) # 预测值

# loss = loss_fn(t_p,t_c) # 预测-实际值差的平方和的均值

# delta = 0.1 # 微小变化量
# learning_rate = 1e-2 # 学习率(0.01)

# loss_rate_of_change_w = \
#         (loss_fn(model(t_u,w+delta,b),t_c)-
#          loss_fn(model(t_u,w-delta,b),t_c)) / (2*delta) # w的损失变化率

# w = w - loss_rate_of_change_w * learning_rate # 更新w(loss_rate_of...为正时减小)

# loss_rate_of_change_b = \
#         (loss_fn(model(t_u,w,b+delta),t_c)-
#          loss_fn(model(t_u,w,b-delta),t_c)) / (2*delta) # b的损失变化率

# b = b - loss_rate_of_change_b * learning_rate # 更新b(loss_rate_of...为正时减小)

def dloss_fn(t_p,t_c):
    dsq_diffs = 2*(t_p - t_c)
    return dsq_diffs

def dmodel_dw(t_u,w,b):
    return t_u

def dmodel_db(t_u,w,b):
    return 1.0

def grad_fn(t_u,t_c,t_p,w,b): # 计算梯度
    dloss_dtp = dloss_fn(t_p,t_c)
    dloss_dw = dloss_dtp * dmodel_dw(t_u,w,b)
    dloss_db = dloss_dtp * dmodel_db(t_u,w,b)
    return torch.stack([dloss_dw.sum(),dloss_db.sum()])

def training_loop(n_epochs,learning_rate,params,t_u,t_c):
    for epoch in range(1,n_epochs+1):
        if params.grad is not None:
            params.grad.zero_() # 清空梯度

        t_p = model(t_u,*params) # 正向传播
        loss = loss_fn(t_p,t_c) # 计算损失
        loss.backward() # 反向传播
        with torch.no_grad():
            params -= learning_rate * params.grad # 优化参数

        if epoch % 500 == 0:
            print('Epoch %d,Loss %f' % (epoch,float(loss)))
            print(f'    Params: {params}')
    return params

t_un = t_u * 0.1 # 输入归一化

# params = training_loop(
#     n_epochs=500,
#     learning_rate=1e-1, # 学习率过大会导致参数震荡（过度训练）
#     params=torch.tensor([1.0,0.0]),
#     t_u=t_un,# 输入归一化
#     t_c=t_c
# )

# t_p: Tensor = model(t_un,*params)

# plt.figure(dpi=128)
# plt.xlabel('Temperature (Fahrenheit)')
# plt.ylabel('Temperature (Celsius)')
# # 实际-预测 折线图
# plt.plot(t_u.numpy(),t_p.detach().numpy()) # 使用tensor.detach()将tensor从计算图中分离出来，不干扰梯度计算
# # 实际-实际 三点图
# plt.plot(t_u.numpy(),t_c.numpy(),'o')
# plt.show()

params = torch.tensor([1.0,0.0],requires_grad=True)

training_loop(
    n_epochs=5000,
    learning_rate=1e-2,
    params=params,
    t_u=t_un,
    t_c=t_c
)
