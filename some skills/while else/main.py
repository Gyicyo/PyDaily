"""
    Create At 2024/3/30
    At:14:56 PM
"""
i = 0
while i < 4:
    print(i)
    i += 1
    if i == 5:
        break
else: # 当while正常结束循环（没有被break）时执行
#相当于是传入了最后一次while判断的if语句？
    print("The loop finished normally")
