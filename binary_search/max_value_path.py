from typing import List
from collections import defaultdict


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        left = 0
        right = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                right = max(right, grid[i][j])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def check_ok(mid):
            visited = [[False] * n for _ in range(m)]
            visited[0][0] = True
            path = [grid[0][0]]
            memo = defaultdict()

            def dfs(i, j):
                if grid[i][j] < mid:
                    return False
                if (i, j) in memo:
                    return memo[(i, j)]
                if i == m - 1 and j == n - 1:
                    mn_v = min(path)
                    if mn_v >= mid:
                        memo[(i, j)] = True
                        return True
                    return False

                for di, dj in dirs:
                    new_i = i + di
                    new_j = j + dj
                    if 0 <= new_i < m and 0 <= new_j < n and not visited[new_i][new_j]:
                        visited[new_i][new_j] = True
                        path.append(grid[new_i][new_j])
                        if dfs(new_i, new_j):
                            visited[new_i][new_j] = False
                            path.pop()
                            memo[(i, j)] = True
                            return True
                        visited[new_i][new_j] = False
                        path.pop()
                return False
            return dfs(0, 0)

        while left < right:  # (]
            mid = left + (right - left + 1) // 2

            if check_ok(mid):
                left = mid
            else:
                right = mid - 1

        return left


class UnionFind:
    def __init__(self, n):
        self.fathers = [x for x in range(n)]

    def find(self, x):
        if self.fathers[x] != x:
            self.fathers[x] = self.find(self.fathers[x])
        return self.fathers[x]

    def union(self, x, y):
        father_x = self.find(x)
        father_y = self.find(y)

        if father_x != father_y:
            self.fathers[father_x] = father_y
        #     return True
        #
        # return False


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)

        vals = [(i, j) for i in range(m) for j in range(n)]

        vals = sorted(vals, key=lambda x: -grid[x[0]][x[1]])

        visited = set()
        dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        for r, c in vals:
            visited.add((r, c))
            for di, dj in dirs:
                new_i, new_j = r + di, c + dj
                if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) in visited:
                    uf.union(r * n + c, new_i * n + new_j)
            if uf.find(0) == uf.find(m * n - 1):
                return grid[r][c]
        return -1


print(Solution().maximumMinimumPath(
    [[3, 4, 6, 3, 4],
     [0, 2, 1, 1, 7],
     [8, 8, 3, 2, 7],
     [3, 2, 4, 9, 8],
     [4, 1, 2, 0, 0],
     [4, 6, 5, 4, 3]]
))
