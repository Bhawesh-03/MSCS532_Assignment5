# performance_test.py

import time
import random
from deterministic_quicksort import quicksort
from randomized_quicksort import randomized_quicksort
import sys

sys.setrecursionlimit(10000)


def test_performance(sort_func, data):
    start = time.time()
    sort_func(data)
    end = time.time()
    return end - start

sizes = [1000, 5000, 10000]
distributions = {
    "Random": lambda n: random.sample(range(n * 10), n),
    "Sorted": lambda n: list(range(n)),
    "Reverse": lambda n: list(range(n, 0, -1))
}

for size in sizes:
    print(f"\nArray Size: {size}")
    for name, dist_func in distributions.items():
        arr = dist_func(size)
        time_det = test_performance(quicksort, arr.copy())
        time_rand = test_performance(randomized_quicksort, arr.copy())
        print(f"{name:10} | Deterministic: {time_det:.5f}s | Randomized: {time_rand:.5f}s")
