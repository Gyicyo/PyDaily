import torch
from torch import hub

resnet18 = hub.load('pytorch/vision:master', 'resnet18', pretrained=True)
