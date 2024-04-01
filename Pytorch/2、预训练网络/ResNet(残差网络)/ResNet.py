from torchvision import models,transforms
import torch
from PIL import Image

resnet = models.resnet101(weights=models.ResNet101_Weights.IMAGENET1K_V1) #引用已训练的Res模型
resnet.eval() #设置为预测模式
preprocess = transforms.Compose([ #定义图像预处理方式
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize( #归一化
        mean=[0.485,0.456,0.406], #均值
        std=[0.229, 0.224, 0.225]), #方差
])

img = Image.open('data/p1ch2/bobby.jpg').convert('RGB') #读取图片并转换为RGB格式
img_t = preprocess(img) #进行预处理（转换图片为模型可识别类型）

batch_t = torch.unsqueeze(img_t, 0) #将图片转换为batch（多出来的维度存储图片数量（用size））

out = resnet(batch_t) #进行预测,返回tensor包含1000个类别的概率值
with open('data/p1ch2/imagenet_classes.txt',encoding='utf-8') as f:
    labels = [line.strip() for line in f.readlines()] #读取标签

_,indexs = torch.sort(out,descending = True) #按tensor内的值进行排序，排序结果为值对应的索引(这里是降序)

percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100 #获取百分比
for p in indexs[0][:5]:
    print(labels[p], percentage[p].item(),"%") # 打印前五个概率最大的类别及其概率
