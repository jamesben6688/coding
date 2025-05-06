class Solution:
    def longest_subseq(self, nums):
        n = len(nums)

        """
            dp[i] = dp[j] + 1
        """
        n = len(nums)
        dp = [[1, [nums[x]]] for x in range(n)]

        # dp[0] = 1

        ans = [1, []]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                # if nums[i] - nums[j] == 1:
                    if 1+dp[j][0] > dp[i][0]:
                        dp[i] = [1+dp[j][0], dp[j][1]+[nums[i]]]
                        if dp[i][0] > ans[0]:
                            ans = dp[i]
        # print(dp)
        # print(dp)
        return ans


print(Solution().longest_subseq(
    [3, 4, 2, 5, 1, 6, 7, 9]
))