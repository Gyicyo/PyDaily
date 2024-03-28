"""
    created at: 2024-03-28
    At: 15:14 PM
"""
#pylint: disable=C0115,C0103,E0401,C0116,C0304
from functools import cache
from functools import lru_cache
from tools import measure

@lru_cache(maxsize=128)
def Fibonacci(n: int):
    if n <= 1:
        return n
    return Fibonacci(n-1) + Fibonacci(n-2)

@measure
def main():
    print(Fibonacci(38))


if __name__ == '__main__':
    main()