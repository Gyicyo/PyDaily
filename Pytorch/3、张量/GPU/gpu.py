import torch
from torch import Tensor
import torchvision

print(torch.cuda.is_available())
print(torch.__version__)

a_t: Tensor = torch.tensor([1, 2, 3], device='cuda',dtype=torch.float32)
print(a_t)
b_t = (a_t * 2).clone()
b_t = b_t.to('cpu',dtype=torch.float32)
print(b_t)
