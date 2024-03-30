"""
    Create At 2024/3/30
    At:20:16 PM
"""

class A:
    name = 'A'

a = A()
name = 4
dic = [(1,2),(3,4)]
print(getattr(dic,'1',5))
print(getattr(a,'name',5))