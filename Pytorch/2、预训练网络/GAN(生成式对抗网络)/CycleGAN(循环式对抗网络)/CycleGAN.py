"""
    Create At 2024/4/1
    At 13:59 PM

"""

#pylint: disable=E0401,W0611,C0103
from torchvision import models,transforms
import torch
from ResNetGenerator import ResNetGenerator
from PIL import Image

netG = ResNetGenerator()
model_path = 'data/p1ch2/horse2zebra_0.4.0.pth'
model_data = torch.load(model_path)
netG.load_state_dict(model_data)
netG.eval()

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.ToTensor()
]) #输入图片预处理

image = Image.open('data/p1ch2/horse.jpg').convert('RGB')
image_t = preprocess(image) #将输入的图片进行预处理
batch_t = torch.unsqueeze(image_t, 0) #将图片转换为batch
batch_out = netG(batch_t) #输出图片
out_t = (batch_out.data.squeeze() +1.0) / 2.0 #归一化
out_image = transforms.ToPILImage()(out_t) #将输出图片保存
out_image.save('data/p1ch2/zebra.jpg') #保存图片
