"""
定义了一类数，如果是质数并且去掉最后一个数位还是这类数

follow up: 找小于n的所有这一类数
"""

class Solution:
    def find_prime(self, n):
        n_digts = 0
        n_copy = n
        while n_copy:
            n_digts += 1
            n_copy = n_copy // 10
        # if n == 1:
        #     return [2, 3, 5, 7]
        ans = []
        base = [2, 3, 5, 7]

        def is_prime(x):
            m = 2
            while m * m <= x:
                if x % m == 0:
                    return False
                m += 1
            return True

        def dfs(l, cur):
            if is_prime(cur) and 1 < cur < n:
                ans.append(cur)
            if l == 0:
                return

            for b in base:
                dfs(l-1, cur * 10 + b)
        print(n_digts)
        dfs(n_digts+1, 0)
        return ans


print(Solution().find_prime(1000))
