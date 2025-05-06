from typing import List
from pprint import pprint


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        """
            dp[i][k] = dp[i-j][k-1] + avg(nums[i-j: i]) s.t. i-j >= k-1 and j >= 1
        """

        n = len(nums)
        dp = [[0.] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, min(i+1, k + 1)):
                for m in range(j-1, i):  # [......., .......]
                    if m > 0 and j-1 == 0:
                        continue

                    dp[i][j] = max(dp[i][j], dp[m][j - 1] + sum(nums[m:i]) / (i - m))
        pprint(dp)
        return dp[-1][-1]


pprint(Solution().largestSumOfAverages(
nums =
[1,2,3,4,5,6,7],
k =
4
))