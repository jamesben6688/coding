from typing import List
from functools import lru_cache

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        MAXN = 13  # 人数最多为 12
        balance = [0] * MAXN

        # 计算每个人的净债务
        for f, t, amt in transactions:
            balance[f] -= amt
            balance[t] += amt

        # 过滤出非 0 的债务
        debt = [b for b in balance if b != 0]
        n = len(debt)

        # dp[mask] 表示当前 mask 中还清的最大分组数
        dp = [-1] * (1 << n)
        dp[0] = 0  # 空集需要0组

        # 子函数：返回当前状态下能组成的最大“内部可清组数”
        def dfs(mask, sum_mask):
            if dp[mask] != -1:
                return dp[mask]

            res = 0
            if bin(mask).count('1') > 1:  # 至少两个元素才能构成交易
                if sum_mask == 0:
                    # 可以组成一组交易，任意去掉一个人，递归子问题 + 1
                    for i in range(n):
                        if (mask >> i) & 1:
                            res = dfs(mask ^ (1 << i), sum_mask - debt[i]) + 1
                            break
                else:
                    # 继续尝试拆分
                    for i in range(n):
                        if (mask >> i) & 1:
                            res = max(res, dfs(mask ^ (1 << i), sum_mask - debt[i]))
            dp[mask] = res
            return res

        full_mask = (1 << n) - 1
        return n - dfs(full_mask, sum(debt))


print(Solution().minTransfers(
    [[0, 1, 10], [2, 0, 5]]
))