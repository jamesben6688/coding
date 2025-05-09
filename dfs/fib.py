import numpy as np

base = np.array([
    [1, 1], [1, 0]
])

first = np.array([1, 0])

def pow(x, n):
    ans = np.ones_like(x)
    while n:
        if n % 2 == 1:
            ans = ans @ x

        x = x @ x
        n = n // 2
    return ans


def get_fib(n):
    return first @ pow(base, n-1)


print(get_fib(4))
