from random import shuffle,sample,choice,choices

list_: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(list_) #随机打乱列表
#print(list_)

names : list[str] = ['Bob','Tom','Jane','Jim']
sampleRes = sample(names,k=8,counts=(2,3,4,5)) # 随机从列表中取k个元素（不重复），并返回一个列表
#counts表示list中每个元素的个数（要求列表中元素个数总和大于k）
#print(sampleRes)

choiceRes = choice(names) # 随机从列表中取一个元素
#print(choiceRes)

choicesRes = choices(names,k=8,weights=[0.2,0.3,0.4,0.1]) # 随机从列表中取k个元素（可重复），并返回一个列表，权重为weights
#weights表示list中每个元素的权重
#print(choicesRes)
