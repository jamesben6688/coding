from functools import cache

class Solution:
    def get_fib(self, n):
        f1 = 1
        f2 = 1
        for i in range(n):
            f1, f2 = f2, f1+f2
        return f1

    @cache
    def get_fib1(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1

        return self.get_fib(n-2) + self.get_fib(n-1)

# 1 1 2 3 5
print(Solution().get_fib(4))
print(Solution().get_fib1(4))