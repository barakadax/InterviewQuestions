# Time O(N) | Mem O(N) - Bottom-Up
def fib_iterative(n: int) -> int:
    res: list[int] = [0, 1]

    for i in range(2, n+1):
        res.append(res[i-1] + res[i-2])

    return res[n]


# Time O(N) | Mem O(N) - Top-Down
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_recursive(n: int) -> int:

    if n <= 1:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Time O(N) | Mem O(1) - In compare with previous iterative doesn't use cache and only uses previous values
def fib_iterative(n: int) -> int:
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


# Time O(Log N) | Mem O(Log N) - Matrix multiplication, binary exponentiation, better for when N value is massive
import numpy as np

def fib_matrix(n: int) -> int:
    if n == 0:
        return 0

    matrix: np.matrix = np.matrix([[1, 1], [1, 0]], dtype=object)
    result: np.matrix = matrix**(n - 1)

    return result[0, 0]


# Time O(Log N) | Mem O(1) - Uses golden ratio calculation, becomes inaccurate after n=71 due to float precision limits
import math

def fib_binet(n: int) -> int:
    phi: float = (1 + math.sqrt(5)) / 2
    psi: float = (1 - math.sqrt(5)) / 2

    return int((phi**n - psi**n) / math.sqrt(5))
