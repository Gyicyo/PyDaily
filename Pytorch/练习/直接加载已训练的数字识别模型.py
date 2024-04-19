import h5py
import torch
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision import transforms
from matplotlib import pyplot as plt
from number import Net

dicts = torch.load('number.pth')
model = Net()
model.load_state_dict(dicts['model'])
model.eval()

pr = transforms.Compose([transforms.ToTensor()])
dataset = MNIST('../data', train=False, download=True, transform=pr)
loader = DataLoader(dataset, batch_size=1, shuffle=False)

for i,(data,target) in enumerate(loader):
    if i > 3:
        break

    output = model(data)
    pred = output.argmax(dim=1, keepdim=True)

    plt.imshow(data[0].view(28,28), cmap='gray')
    plt.title('Prediction: %d' % pred.item())
    plt.show()
