def fib(num):
    a,b = 0,1
    for _ in range(num):
        a,b = b,a+b
        yield a

print(list(fib(10)))