"""
    created at: 2024-03-28
    At: 23.29 PM
"""
#pylint: disable=C0115,C0103,E0401,C0116,C0304
from functools import singledispatch

@singledispatch
def func(arg):
    return f'Default:{arg}'

@func.register
def _(arg: str):
    return f'String:{arg}'

@func.register
def _(arg: int):
    return f'Integer:{arg}'

print(func('Hello'))
print(func(123))
print(func(1.9))