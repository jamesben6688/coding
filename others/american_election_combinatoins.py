from pprint import pprint
def fin_domb(nums, target):
    n = len(nums)
    s = sum(nums)

    ans = 0
    dp = [[0 for _ in range(s+1)] for i in range(n+1)]

    # dp[i][j] top i states, win j votes

    for i in range(n+1):
        dp[i][0] = 1

    for j in range(1, s+1):
        for i in range(1, n+1):
            dp[i][j] = dp[i-1][j]
            if j-nums[i-1] >= 0:
                dp[i][j] += dp[i-1][j-nums[i-1]]
    for i in range(target, s+1):
        ans += dp[-1][i]
    return ans

"""
    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
"""
print(fin_domb([2,4,7], 5))

"""
7
2 4
2 7
4 7
2 4 7
"""
