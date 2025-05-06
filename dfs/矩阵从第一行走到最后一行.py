from functools import cache, lru_cache

class Solution:
    def paths(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        visited = set()
        path = []
        ans = []

        @lru_cache
        def dfs(i, j):
            nonlocal ans
            if i == m-1:
                ans.append((path + [(i, j)])[:])
                return True

            path.append((i, j))
            visited.add((i, j))
            for di, dj in dirs:
                ii = i + di
                jj = j + dj
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in visited and matrix[ii][jj] == 1:
                    dfs(ii, jj)
                    # if dfs(ii, jj):
                    #     return True
            visited.remove((i, j))
            path.pop()
            return False

        for i in range(n):
            if matrix[0][i] == 1 and dfs(0, i):
                pass
                # return True, ans
        return ans, len(ans)
        # return False, []


print(Solution().paths(
    [[0, 1, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1]]

# [[0, 1, 0, 1, 1],
# [0, 1, 1, 0, 1],
# [0, 0, 0, 1, 0],
# [0, 0, 0, 1, 1]]
))
