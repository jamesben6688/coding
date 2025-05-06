from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
            dp[i][d] = dp[j][d] + 1 if nums[i] - nums[j] == d

            dp[i][d] 表示以nums[i]结尾, 公差为d, 长度>=2的数目。方便计算。如果>=3, 则还需要初始化的时候做更多复杂操作
        """
        n = len(nums)
        dp = [defaultdict(int) for i in range(len(nums))]
        ans = 0
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] += dp[j][d] + 1

                ans += dp[j][d]  # 直接把nums[i]接到nums[j]后面, 变成公差为d, 长度>=3的数目

        return ans


print(Solution().numberOfArithmeticSlices([2, 4, 6, 8]))