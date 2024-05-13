from functools import partial,wraps

# class me:
#     def __init__(self,name):
#         self.name = name

# m = me('Hel')
# print(m.__dict__)
# m.age = 20
# print(m.__dict__)

# def hello(self):
#     print(self.q)

# hello.q = 2
# print(hello.__dict__)
# hello = partial(hello,hello)
# hello()

def outer_with_wraps(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return inner

def outer_without_wraps(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return inner

@outer_with_wraps
def add(x, y):
    print(add.__name__)
    return x + y

@outer_without_wraps
def pow(x,y):
    print(pow.__name__)
    return x ** y

add(x=1,y=2)
pow(x=1,y=2)
