import torch
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
import logging

logging.basicConfig(level=logging.INFO,filename='log.log')

def normalize(x):
    return (x - x.min()) / (x.max() - x.min())


num_samples = 10000

grades_t = torch.rand(num_samples) * 100 + 50
result_t =  (grades_t > grades_t.max()*0.8).float()

grades_t = normalize(grades_t)

dataset = TensorDataset(grades_t, result_t)
loader = DataLoader(dataset, batch_size=32, shuffle=True)

class LogisticRegressionModel(nn.Module):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.linear = nn.Linear(1, 1)

    def forward(self,x):
        logging.info(f"Input: {x.max().item()}")
        logging.info(f"Input: {x.min().item()}")
        pred = self.linear(x)
        precentages = torch.sigmoid(pred)
        logging.info(f"Output: {precentages[x.argmax()].item()}")
        logging.info(f"Output: {precentages[x.argmin()].item()}")
        return precentages

model = LogisticRegressionModel()
print(next(model.parameters()))
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=1) # 这里学习率对结果影响似乎并不大？而且似乎学习率越高越好？

def train(epochs):
    for epoch in range(1, epochs+1):
        model.train()
        for (grades, result) in loader:
            optimizer.zero_grad()
            output = model(grades.unsqueeze(1))
            loss = criterion(output.view(-1), result)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch}/{epochs}, Loss: {loss.item():.4f}, Weights: {model.linear.weight.item():.4f}")

train(20)
text = torch.tensor([[50.0], [60.0], [110.0], [140.0], [118.0]])
text = normalize(text)
print(model(text).float())
print(model.state_dict())
