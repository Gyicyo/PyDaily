"""
    Create At 2024/3/30
    At:14:21 PM
"""

a = True
b = False
c = True
d = False

li: list = [a, b, c, d]

if all(li):
    print("All are True")
else:
    print("Not all are True")

if any(li):
    print("At least one is True")

else:
    print("None is True")
