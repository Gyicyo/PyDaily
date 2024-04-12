class A:
    __slots__ = ('_a', 'b')
    def __init__(self, a, b):
        self._a = a
        self.b = b

    @property
    def a(self):
        print('Getting a')
        return self._a

    @a.setter
    def a(self, value):
        print('Setting a to', value)
        self._a = value

a: A = A(1, 2)
print(a.a)
a.a = 3
