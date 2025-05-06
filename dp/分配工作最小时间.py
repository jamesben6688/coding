from functools import cache
from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
            题解:
                https://www.bilibili.com/video/BV1jX4y1K7Ur/?spm_id_from=333.337.search-card.all.click&vd_source=515dedd17a7416a93307429c1b2dfa6b

                dp[i][state] = max(dp[i-1][subset])
        """
        n = len(jobs)
        times = [0 for _ in range(k)]
        ans = float('inf')

        # @cache
        def f(status, i):
            """
                当前状态status, 开始分配第i个工作
            """
            nonlocal ans
            if status == 0:
                ans = min(ans, max(times))
                return
            flag = 0
            for j in range(k):
                if times[j] == 0:
                    if flag == 1:
                        return
                    else:
                        flag = 1
                times[j] += jobs[i]
                f(status ^ (1 << i), i + 1)
                times[j] -= jobs[i]

        f((1 << n) - 1, 0)
        return ans
        # n = len(jobs)
        # states = (1 << (n+1)) - 1

        # dp = [[float('inf') for _ in range(states)] for i in range(n)]

        # for i in range(1, k):
        #     sub_state = 0
        #     while sub_state:
        #         dp[i][]


print(Solution().minimumTimeRequired(
jobs = [20010,20006,20014,20004,20008,20006,20005,20012,19999,20014,20003,20012], k = 8
))
# 19999, 20003, 20004, 20005, 20006, 20006, 20008, 20010, 20012, 20014, 20014, 11
# 19999 + 20003, 20004+20005, 20006+20006, 20008