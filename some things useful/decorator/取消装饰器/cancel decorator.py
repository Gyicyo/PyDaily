from functools import partial,wraps

def out(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling function: ", func.__name__)
        return func(*args, **kwargs)

    return wrapper

@out
def add(x, y):
    return x + y

add = add.__wrapped__

print(add(2, 3))
