"""
    created at: 2024-03-28
    At: 13.15 PM
"""
from timeit import repeat
import gc

gc.disable()

ADD1 = """
list = [i for i in range(10)]
"""

ADD2 = """
list = []
for p in range(10):
    list.append(p)
"""



if __name__ == '__main__':
    print("Start...")
    Wramup = min(repeat(ADD2,repeat=5,number=1000000))
    print(f"Wramup time: {Wramup:.3f}s")
    t1 = min(repeat(ADD1,repeat=5,number=1000000))
    t2 = min(repeat(ADD2,repeat=5,number=1000000))
    print(f"ADD1 time: {t1:.3f}s")
    print(f"ADD2 time: {t2:.3f}s")
