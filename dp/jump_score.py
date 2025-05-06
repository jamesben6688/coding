"""
一个一维数组[3,10,2,12] 判断从起始点0到最后终点的最大分数，每次跳跃格数任意（1格或者直接跳到最后），
score = 目的地的 score * distance，比如直接跳到最后分数是 12*3 = 36， 如果一格格跳是10+2+12 = 24。
 用dp做的，小哥提示后发现greedy也可以

"""

def get_max_score(nums):
    n = len(nums)
    dp = [0] * n

    for i in range(1, n):
        for j in range(i):
            dp[i] = max(dp[i], dp[j] + (i-j)*nums[i])
    print(dp)
    return dp[-1]


print(get_max_score([1, 20, 100, 30, 20, 10, 40]))
