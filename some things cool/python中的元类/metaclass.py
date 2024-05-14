class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print("MyMeta.__new__ called at:",name)
        print(attrs)
        for k,v in attrs.items():
            if isinstance(v, int):
                print(f"{k} is int")
                v = v*10
                attrs[k] = v
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=MyMeta):
    a = 10


cl = MyClass()
print(cl.a)
