"""
Recently I faced this question
Suppose here are a given array [1,5,12,20] and max=7
We need to making all the values from 1 to max
So find the smallest coins to make from all the value 1 to max
Here if I use 7 coins of 1 dollar we can easily make all the value from 1 to 7 -So 7 coins needed here
If I use 4 coins of 1 dollar and 1 coins of 5 dollar we can also make all the value from 1 to 7- Here 5 coins needed
So my smallest answer is 5 not 7

How can I solve this problem? Do you have any idea?

dp[i] = dp[j] + 1
"""

class Solution:
    def get_min_coins(self, nums, m):
        dp = [float('inf')] * (m+1)
        nums = set(nums)
        for i in range(m+1):
            if i in nums:
                dp[i] = 1
            else:
                for j in range(i):
                    if i-j in nums:
                        dp[i] = min(dp[i], dp[j]+1)
        print(dp)
        return max(dp[1:])


print(Solution().get_min_coins([1, 5, 12, 20], m=7))
