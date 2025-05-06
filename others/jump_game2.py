class Solution:
    def jump(self, nums):
        n = len(nums)
        dp = [float('inf') for _ in range(len(nums))]
        dp[0] = 0

        for i in range(n):
            for j in range(i+1, min(n-1, i+nums[i])+1):
                if dp[i] % 2 == 0 and (j - i) % 2 == 0:
                    dp[j] = min(dp[j], dp[i]+1)

                if dp[i] % 2 == 1 and (j - i) % 2 == 1:
                    dp[j] = min(dp[j], dp[i]+1)

        return dp[-1], dp


print(Solution().jump([2,3,1,1,4]))
