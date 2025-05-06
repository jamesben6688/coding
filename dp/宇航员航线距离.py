class Solution:
    def max_distance(self, arr, k):
        """
            dp[i][j] = max(dp[i-1][j+1]+arr[i], dp[i-1][j-1])

        :param arr:
        :param k:
        :return:
        """
        if k == 0: return 0

        n = len(arr)
        dp = [[0] * (k+1) for _ in range(n+1)]

        for i in range(n):
            for j in range(k):
                # print(i, j)
                # if i==3 and j==0:
                #     print("")
                if j == 0:
                    dp[i+1][j] = dp[i][j+1]+arr[i]
                elif j == k:
                    dp[i+1][j] = dp[i][k]
                else:

                    dp[i+1][j] = max(dp[i][j+1]+arr[i], dp[i][j-1])

        return max(dp[-1])

print(Solution().max_distance(arr = [5, 2, 4, 1, 3], k=3))
print(Solution().max_distance(arr = [6, 7, 8, 5, 4, 3], k = 2))
print(Solution().max_distance(arr = [0, 0, 0, 0], k = 2))
print(Solution().max_distance(arr = [1, 1, 1, 1, 1], k = 5))
print(Solution().max_distance(arr = [10, 1, 1, 10, 1],k = 2))