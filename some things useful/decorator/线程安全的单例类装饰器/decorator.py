from functools import wraps
from threading import RLock

def singleton(cls):
    print("singleton")
    instances = {}
    lock = RLock()
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class a:
    def __init__(self,x):
        self.x = x

