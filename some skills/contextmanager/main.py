"""
    created at: 2024-03-28
    At: 23.29 PM
"""
#pylint: disable=C0115,C0103,E0401,C0116,C0304
from contextlib import contextmanager

def do_something():
    return 0  # 假设返回一个资源对象

def do_otherthing():
    ...

def do_something_with(resource):#pylint: disable=W0613
    ...

@contextmanager
def managed_resource():
    resource = do_something()  # 进入上下文时执行的操作，比如打开文件或连接数据库
    try:
        yield resource  # 在此处yield，被with语句块捕获的值可在此处使用
    finally:
        do_otherthing()  # 退出上下文时执行的操作，比如关闭文件或断开数据库连接

# 使用示例：
with managed_resource() as r:
    # 在这里使用resource，这段代码会在managed_resource的yield表达式之后执行
    do_something_with(r)

# 当离开with语句块时，会自动调用managed_resource生成器函数内的finally部分，完成清理工作