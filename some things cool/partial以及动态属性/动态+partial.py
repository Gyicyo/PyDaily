from functools import partial,wraps

class me:
    def __init__(self,name):
        self.name = name

m = me('Hel')
print(m.__dict__)
m.age = 20
print(m.__dict__)

def hello(self):
    print(self.q)

hello.q = 2
print(hello.__dict__)
hello = partial(hello,hello)
hello()
