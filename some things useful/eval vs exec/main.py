"""
    Create At 2024/3/30
    At:14:56 PM
"""

s: str = """
1+2
"""
r = eval(s)
print(f'This is r:{r},from eval')

r = exec(s)
print

s = "import math"
exec(s)
print(math.pi)