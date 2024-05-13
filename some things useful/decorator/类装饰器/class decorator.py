from functools import partial,wraps
from typing import Any
import time

class record:
    def __init__(self, output):
        self.output = output

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            self.output('spent:',time.time() - start,'s')
            return res
        return wrapper

@record(print)
def add(a, b):
    return a + b

add(1,2)
