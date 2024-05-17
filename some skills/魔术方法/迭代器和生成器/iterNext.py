class A:

    def __init__(self, num):
        self.num = num
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        print("Iterating...")
        if self.idx < self.num:
            self.idx += 1
            return self.idx
        raise StopIteration()

a = A(10)
print(list(a))