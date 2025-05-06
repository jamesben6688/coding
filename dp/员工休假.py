from typing import List

"""
题解: https://leetcode.cn/problems/maximum-vacation-days/solutions/2585287/568-zui-da-xiu-jia-tian-shu-by-stormsuns-lqb1/
"""
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        """
            dp[i][j]表示第i天在城市j的最大天数

            1. 第i天不动 dp[i][j] = dp[i-1][j] + days[i-1][j]

            2. 第i从从别的城市飞过来
                dp[i][j] = dp[i-1][k] + days[i-1][k] s.t. flights[k][i] == 1 and days[i-1][k] > 0
        """

        cities = len(days)
        total_days = len(days[0])

        dp = [[-1] * cities for i in range(total_days+1)]

        # for i in range(cities):
        dp[0][0] = 0

        for i in range(1, total_days+1):
            for j in range(cities):
                if dp[i-1][j] != -1:
                    dp[i][j] = dp[i-1][j] + days[j][i-1]
                for kk in range(cities):
                    if flights[kk][j] == 1 and kk != j and dp[i-1][kk] > -1:
                        dp[i][j] = max(dp[i][j], dp[i-1][kk]+days[j][i-1])

        print(dp)
        return max(dp[-1])


print(Solution().maxVacationDays(
flights =
[[0,1,1],
 [1,0,1],
 [1,1,0]],
days =
[[1,3,1],
 [6,0,3],
 [3,3,3]]
))