from bisect import bisect_right
"""
Max profit for growing crops，给定几种庄稼的种类，grow time period，profit；给定一块地，一次只能种一种庄稼，
1235
给定一个时长，问如何最大化收益。
时长，比如总共有一年或者一个月的期限，在这个期限的最后你能拿到的最大利益，
对的每种庄稼只给出来growtime，比如10天，startTime和endTime是你要optimize的。
"""

def max_crop_profit(crops, total_time):
    crops.sort(key=lambda x: x[1])  # 按结束时间排序
    n = len(crops)
    ends = [crop[1] for crop in crops]

    # pre[i]: the last non-overlapping crop index before i
    pre = []
    for i in range(n):
        start_i = crops[i][0]
        idx = bisect_right(ends, start_i) - 1
        pre.append(idx)

    # dp[i][t]: max profit for first i crops using time <= t
    dp = [[0] * (total_time + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        start, end, profit = crops[i - 1]
        duration = end - start
        for t in range(total_time + 1):
            # 不选第i个
            dp[i][t] = dp[i - 1][t]
            # 如果能选第i个
            if duration <= t:
                dp[i][t] = max(
                    dp[i][t],
                    dp[pre[i - 1] + 1][t - duration] + profit
                )
    return dp[n][total_time]
