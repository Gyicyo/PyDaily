import imageio
import torch
import os

# 加载单张图片
img_arr = imageio.v3.imread('data/p1ch2/bobby.jpg')
print(img_arr.shape)
img = torch.from_numpy(img_arr)
# pytorch要求张量排列为(channels, height, width)
out = img.permute(2, 0, 1) # (height, width, channels)->(channels, height, width)
print(out.shape)


#加载多张图片
batch_size = 3
batch = torch.zeros(batch_size, 3, 256, 256,dtype=torch.uint8)

data_dir = 'data/p1ch4/image-cats'
filenames = [name for name in os.listdir(data_dir)
            if os.path.splitext(name)[1] in ['.jpg', '.png']]
for i,filename in enumerate(filenames):
    img_arr = imageio.v3.imread(os.path.join(data_dir, filename))
    img_t = torch.from_numpy(img_arr)
    img_t = img_t.permute(2, 0, 1)
    img_t = img_t[:3] # 只保留三个通道，因为有的图片还有透明度通道
    batch[i] = img_t

# batch = batch.float() / 255.0 # 归一化到0-1之间
#归一化为正态分布
batch = batch.float()
n_channels = batch.shape[1]
for c in range(n_channels):
    mean = batch[:,c].mean()
    std = batch[:,c].mean()
    batch[:,c] = (batch[:,c] -mean)
print(batch)
