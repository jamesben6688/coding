class Solution:
    def num_paths(self, m, n, grids):
        ans = 0
        # m = len(grid)
        # n = len(grid[0])
        dirs = [(-1, 1), (1, 1), (0, 1)]

        def dfs(i, j):
            nonlocal ans
            if i == m - 1 and j == n - 1:
                ans += 1
                return
            if not (0 <= i < m and 0 <= j < n):
                return
            for di, dj in dirs:
                new_i, new_j = i + di, j + dj
                dfs(new_i, new_j)

        dfs(m - 1, 0)
        return ans

    def num_paths_1(self, m, n, grid=None):
        dp = [[0 for _ in range(n)] for i in range(m)]

        """
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1] + dp[i+1][j-1]
        """

        # init

        dp[m-1][0] = 1

        for j in range(1, n):
            for i in range(m):
                dp[i][j] += dp[i][j-1]
                if i == 0:
                    dp[i][j] += dp[i+1][j-1]
                elif i == m-1:
                    dp[i][j] += dp[i-1][j-1]
                else:
                    dp[i][j] += dp[i+1][j-1] + dp[i-1][j-1]

        return dp[-1][-1]


print(Solution().num_paths_1(3, 3, None))
