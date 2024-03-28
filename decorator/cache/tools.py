"""
    created at 2024.3.28
    At 18:59 PM
"""

from typing import Callable
import time

def measure(func:Callable):
    """
    执行时间装饰器
"""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        used_time = end_time - start_time
        print(f"Function {func.__name__} used: {used_time*1000:.2f} ms")
        return result
    return wrapper
