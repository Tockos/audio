
import matplotlib.pyplot as plt
from random import randint
from timeit import repeat

from merge import *
from insert import *
from bubble import *
from quick import *

NUMBER = 1
SIZE = 1000
STEP = 100

def test(method, array):
    setup = f"from __main__ import {method}" if method != 'sorted' else ''
    stmt = f"{method}({array})"
    return min(repeat(stmt=stmt, setup=setup, number=NUMBER))


methods = ['sorted', 'insert', 'insert_bisect', 'merge_sort', 'quick']

results = []
try:
    for size in range(10, SIZE, STEP):
        array = [randint(0, size) for _ in range(size)]
        result = tuple(test(m, array) for m in methods)
        results.append(result)
        print(f"Size {size}: {result}")
except KeyboardInterrupt:
    pass


for idx, method in enumerate(methods):
    x = [i*STEP for i in range(len(results))]
    y = [r[idx] for r in results]
    plt.plot(x, y, label=method, marker='o', linestyle='dotted')


plt.legend()
plt.grid(True)
plt.show()


