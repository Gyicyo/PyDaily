"""
    Create At 2024/3/30
    At:20:16 PM
"""
from functools import reduce

l = ['a1','b2','c3','d4']
numbers = [1,2,3,4,5]

string: str = reduce(lambda x,y: f'{x}-{y}', l)
print(string)
num = reduce(lambda x,y: x+y, numbers)
print(num)
