import torch
import matplotlib.pyplot as plt
import numpy as np

height_t = torch.tensor([[152,14],[156,14],[160,15],[164,15],[168,16],[172,17],[176,18],[180,18],[184,19],[188,21]],dtype=torch.float)
weight_t = torch.tensor([51,53,54,55,57,60,62,65,69,72],dtype=torch.float)


# 将数据转换为NumPy数组进行预处理
height_np = height_t.numpy()
weight_np = weight_t.numpy()

# 使用NumPy进行最小-最大缩放（Min-Max Scaling）
height_min = height_np.min(axis=0)
height_max = height_np.max(axis=0)
weight_min = weight_np.min()
weight_max = weight_np.max()

height_un = (height_np - height_min) / (height_max - height_min)
weight_un = (weight_np - weight_min) / (weight_max - weight_min)

# 转换回PyTorch张量
height_un_t = torch.from_numpy(height_un)
weight_un_t = torch.tensor(weight_un, dtype=torch.float)

# 确保数据已归一化到[0, 1]区间
assert (height_un_t >= 0).all() and (height_un_t <= 1).all()
assert (weight_un_t >= 0).all() and (weight_un_t <= 1).all()


class LinearModel(torch.nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x):
        pred = self.linear(x)
        return pred

model = LinearModel()
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(10000):
    y_pred = model(height_un_t) # batch_size , 1
    loss = criterion(y_pred, weight_t)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if epoch % 100 == 0:
        print(f"Epoch {epoch+1} loss: {loss.item()}")

print(f"Weight: {model.linear.weight} Bias: {model.linear.bias.item()}")

data = torch.tensor([172,17],dtype=torch.float)
data_un = (data - height_min) / (height_max - height_min)

pred = model(data_un)
pred_u = pred.item() * (weight_max - weight_min) + weight_min
print(f"Predicted weight: {pred}")
