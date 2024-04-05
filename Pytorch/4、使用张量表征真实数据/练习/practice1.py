import torch
import os
from PIL import Image
import numpy as np
import torchvision.transforms as transforms

batch_size = 3
data_dir = "practice"
target_size = (256, 256) #放缩大小
batch = torch.zeros(batch_size, 3, 256, 256,dtype=torch.uint8) # 批次,处理图像dtype一定要调unit.8

filenames = [name for name in os.listdir(data_dir)
             if name.split('.')[-1] in ['png', 'jpg', 'jpeg']] # 获取所有图像

for i,name in enumerate(filenames): # 将图像逐个添加到批次
    img_pil = Image.open(os.path.join(data_dir, name)).convert('RGB') # 打开图像，并转为三通道
    resized_img = img_pil.resize(target_size)

    resized_img_arr = np.array(resized_img)
    img = Image.fromarray(resized_img_arr)
    img_t = torch.from_numpy(resized_img_arr).permute(2,0,1)
    img = transforms.ToPILImage()(img_t)
    batch[i] = img_t

for p in batch:
    print(p.shape)
    #获取图像亮度
    # print(f'Brightness:{p.mean().item():.0f}')
    # print(f'R:{p[0].mean():.0f},G:{p[1].mean():.0f},B:{p[2].mean():.0f}')
    img = transforms.ToPILImage()(p)
    img.show()
