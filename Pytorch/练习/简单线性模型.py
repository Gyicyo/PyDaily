import torch
import matplotlib.pyplot as plt

height_t = torch.tensor([152,156,160,164,168,172,176,180,184,188],dtype=torch.float)
weight_t = torch.tensor([51,53,54,55,57,60,62,65,69,72],dtype=torch.float)
print(height_t.size())
class LinearModel(torch.nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred

model = LinearModel()
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)

for epoch in range(10000):
    y_pred = model(height_t.unsqueeze(1)) # batch_size , 1
    loss = criterion(y_pred, weight_t.unsqueeze(1))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if epoch % 100 == 0:
        print(f"Epoch {epoch+1} loss: {loss.item()}")

print(f"Weight: {model.linear.weight.item()} Bias: {model.linear.bias.item()}")

plt.scatter(height_t.numpy(), weight_t.numpy())
plt.plot(height_t.numpy(), model(height_t.unsqueeze(1)).detach().numpy(), color='r')
plt.show()
