from functools import cache
from typing import List
import math

class Solution:
    def minimumTimeRequired(self, jobs: List[List[int]],) -> int:
        """
            题解:
                https://www.bilibili.com/video/BV1jX4y1K7Ur/?spm_id_from=333.337.search-card.all.click&vd_source=515dedd17a7416a93307429c1b2dfa6b

                dp[i][state] = max(dp[i-1][subset])
        """
        n = len(jobs)
        k = len(jobs[0])

        ans = math.inf
        cost = 0
        from copy import deepcopy

        assigned = [[] for _ in range(k)]
        ans_assign = None
        # @cache
        def f(i):
            """
                当前状态status, 开始分配第i个工作
            """
            nonlocal cost, ans, ans_assign
            if cost >= ans:
                return
            if i == n:
                ans = min(ans, cost)
                ans_assign = deepcopy(assigned)

            for j in range(k):
                if len(assigned[j]) < k:
                    assigned[j].append(i)
                    cost += jobs[i][j]
                    f(i+1)
                    cost -= jobs[i][j]
                    assigned[j].pop()

        f(0)
        return ans, ans_assign


print(Solution().minimumTimeRequired(
    jobs=[
          [5, 1],
          [3, 6],
          [4, 2],
          [2, 8]
]


))
# 19999, 20003, 20004, 20005, 20006, 20006, 20008, 20010, 20012, 20014, 20014, 11
# 19999 + 20003, 20004+20005, 20006+20006, 20008