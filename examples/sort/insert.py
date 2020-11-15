
import functools as ft
from bisect import insort

def insert_bisect(array):
    if len(array) < 2:
        return array

    result = []
    for old in array:
        insort(result, old)
    return result


def insert(array):
    if len(array) < 2:
        return array

    result = [array[0]]
    for old in array[1:]:
        idx = next((i for i, new in enumerate(result) if new > old), len(result))
        result.insert(idx, old)

    return result


if __name__ == "__main__":
    from timeit import repeat
    from random import randint
    MAX = 1000
    array = [randint(0, MAX) for _ in range(MAX)]
    best = min(repeat(stmt=lambda: insert_bisect(array), number=1000))
    print(f"insert_bisect: {best}")

    best = min(repeat(stmt=lambda: insert(array), number=1000))
    print(f"insert: {best}")

