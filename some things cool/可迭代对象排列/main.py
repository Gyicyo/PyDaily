"""
    Create At 2024/3/30
    At:14:56 PM
"""
from itertools import permutations

l: tuple = [1,2,3]
#l的全排列
print(list(permutations(l)))
#l的部分排列
print(list(permutations(l, 2)))
