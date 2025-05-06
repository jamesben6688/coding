sx = []
sy = []

"""
    dp[i][0] = dp[i-1][0] + sx[i]
    dp[i][0] = dp[i-1][1] + sy[i] - amount
    
    dp[i][1] = dp[i-1][1] + sy[i]
    dp[i][1] = dp[i-1][0] + sx[i] - amount
    
    return max(dp[-1])
    
"""