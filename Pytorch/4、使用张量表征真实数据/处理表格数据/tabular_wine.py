import torch
import numpy as np
import csv

wineq_path = "data/p1ch4/tabular-wine/winequality-white.csv"
wineq_numpy = np.loadtxt(wineq_path, delimiter=";",dtype=np.float32,
                        skiprows=1)
# print(wineq_numpy.shape)
# print(wineq_numpy)
col_list = next(csv.reader(open(wineq_path), delimiter=';'))
#print(col_list) # 检查是否提取完毕
wineq = torch.from_numpy(wineq_numpy)

data = wineq[:,:-1] # 特征数据
target = wineq[:,-1].long() # 标签数据

# 标签数据one-hot编码
# target_onehot = torch.zeros(target.shape[0],10) # 总共10个数
# target_onehot.scatter_(1, target.unsqueeze(1), 1.0) # 第二个参数为索引张量（用于提供索引），需要与我们散射用到的张量具有相同的维度

# data_mean = data.mean(dim=0) # 计算特征数据的均值
# data_var = data.var(dim=0) # 计算特征数据的方差
# data_normalized = (data - data_mean) / data_var.sqrt() # Z-score标准化特征数据

# bad_data = data[target<=3] # 布尔索引
# mid_data = data[(target>3) & (target<7)]
# good_data = data[target>=7]
# 获取均值
# bad_mean = bad_data.mean(dim=0)
# mid_mean = mid_data.mean(dim=0)
# good_mean = good_data.mean(dim=0)

# 打印结果，看看哪个特征影响较大（这里首先找到了劣质酒二氧化硫含量较高）
# for i,args in enumerate(zip(col_list,bad_mean,mid_mean,good_mean)):
#     print(f"{i:2}.{args[0]:20}: {args[1]:6.2f}, {args[2]:6.2f}, {args[3]:6.2f}")

total_sulfur_threshold = 141.83
total_sulfur_data = data[:,6]
predicted_indexes = torch.lt(total_sulfur_data, total_sulfur_threshold)#比较，返回bool的Tensor
#ge: >= , gt: > , lt: < , le: <=
print(predicted_indexes.sum()) # 只根据二氧化硫值预测的优质酒数量（2727）
actual_indexes = target > 5
print(actual_indexes.sum()) # 实际优质酒数量（3258）

n_matches = (predicted_indexes & actual_indexes).sum() # 预测正确的数量,这里使用位运算，因为 == 只适用于二者数量相等
n_predicted = predicted_indexes.sum() # 预测数量
n_actual = actual_indexes.sum() # 实际优质酒数量
print((n_matches/n_predicted).item()) # 精确率 预测是优质酒，是优质酒的概率是74%
print(f"Accuracy: {n_matches/n_actual:.4f}") # 预测正确的概率是61%
