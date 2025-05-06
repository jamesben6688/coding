from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans = 0
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for i in range(m)]
        t = m * n
        def dfs(i, j):
            nonlocal ans, t
            if grid[i][j] == 2:
                # print(f"t: {t}")
                if t == 1:
                    ans += 1
                return

            for di, dj in dirs:
                ii = i + di
                jj = j + dj
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] != -1 and not visited[ii][jj]:
                    visited[ii][jj] = True
                    t -= 1
                    dfs(ii, jj)
                    t += 1
                    visited[ii][jj] = False

        start_i, start_j = -1, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    t -= 1
                if grid[i][j] == 1:
                    start_i = i
                    start_j = j
        visited[start_i][start_j] =True
        dfs(start_i, start_j)
        return ans


print(Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))