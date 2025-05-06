class Solution:
    def uniquePaths_1(self, m: int, n: int) -> int:
        ans = 0
        dirs = [(0, 1), (-1, 1), (1, 1)]
        def dfs(i, j):
            nonlocal ans
            if i == m-1 and j == n-1:
                ans += 1

            for d in dirs:
                ii = i + d[0]
                jj = j + d[1]

                if 0 <= ii < m and 0 <= jj < n:
                    dfs(ii, jj)

        dfs(0, 0)
        return ans

    def uniquePaths(self, m: int, n: int) -> int:
        dirs = [(0, 1), (-1, 1), (1, 1)]
        dp = [[0 for _ in range(n)] for i in range(m)]
        for i in range(n):
            dp[0][i] = 1
        """
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1] + dp[i+1][j-1]
        """
        for j in range(1, n):
            for i in range(1, m):
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

                if i < m-1:
                    dp[i][j] += dp[i+1][j-1]
        # print(dp[-1][-1])
        return dp[-1][-1]

print(Solution().uniquePaths_1(3, 3))
