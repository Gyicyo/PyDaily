"""
    Create At 2024/3/31
    At:16:01 PM
"""
x = 5

def global_():
    global x
    x += 1

global_()
print(x) # 6

def nonlocal_():
    x = 1
    def inner():
        nonlocal x # 获取上一层的函数内变量
        x += 1

    inner()
    print(x) # 2

nonlocal_()
