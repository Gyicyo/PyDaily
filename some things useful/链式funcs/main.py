"""
    Create At 2024/3/30
    At:14:35 PM
"""
from typing import Callable

def func3(b: bool) -> Callable:
    print(f'{b = }')

def func2(a: int) -> Callable:
    print(f'{a = }')
    return func3
def func1(string: str) -> Callable:
    print(string)
    return func2

func1('hello')(2)(True)