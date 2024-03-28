"""
    created at: 2024-03-28
    At: 15:14 PM
"""

from itertools import batched

LIST: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
batch: batched = batched(LIST, 3)

print(list(batch))
