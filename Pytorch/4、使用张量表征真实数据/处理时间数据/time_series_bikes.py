import numpy as np
import torch

bikes_numpy = np.loadtxt("data/p1ch4/bike-sharing-dataset/hour-fixed.csv",
                         delimiter=",",
                         skiprows=1,
                         dtype=np.float32,
                         converters={1: lambda x: float(x[8:10])}) # 将日期字符串转换为day
bikes = torch.from_numpy(bikes_numpy)
print(bikes.shape)

# 使用view不会有任何张量被复制，只用于改变张量查看存储的相同数据的方式
daily_bikes = bikes.view(-1,24,bikes.shape[1])#-1作为占位符，自动计算
# print(daily_bikes.stride())
daily_bikes = daily_bikes.transpose(1,2)
print(daily_bikes.shape)

# weather独热编码

# 仅第一天
first_day = bikes[:24,9].long()
weather_onehot = torch.zeros(first_day.shape[0], 4)
weather_onehot.scatter_(1, first_day.unsqueeze(1)-1, 1.0) # -1 是因为weather是1~4，索引从0开始
print(torch.cat((bikes[:24],weather_onehot),1).shape) # 合并weather_onehot和bikes

# 所有
daily_weather_onehot = torch.zeros(daily_bikes.shape[0], 4 ,daily_bikes.shape[2])
daily_weather_onehot.scatter_(1,daily_bikes[:,9,:].long().unsqueeze(1)-1,1.0)
daily_bikes = torch.cat((daily_bikes,daily_weather_onehot),dim=1)

#另外一种weather处理方式（视为连续变量）
# daily_bikes[:,9,:] = (daily_bikes[:,9,:] - 1.0) / 3.0 # 归一化到[0,1]
#将数据范围调整到[-1,1]或[0,1]对训练是有利的
print(daily_bikes.shape)

# temp归一化
temp = daily_bikes[:,10,:]
temp_min = temp.min()
temp_max = temp.max()
daily_bikes[:,10,:] = ((daily_bikes[:,10,:] - temp_min)
                        / (temp_max - temp_min)) # 映射到[0,1]

#或者也可以映射到[-1,1](减均值再除以标准差)
temp_mean = temp.mean()
temp_std = temp.std()
daily_bikes[:,10,:] = ((daily_bikes[:,10,:] - temp_mean)
                        / temp_std) # 映射到[-1,1]
