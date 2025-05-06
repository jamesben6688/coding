from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        """
            洪水填充
        """
        m = len(grid)
        n = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        border = []

        def dfs(i, j, c):
            visited.add((i, j))
            is_border = False
            for di, dj in dirs:
                new_i, new_j = i + di, j + dj
                if (new_i, new_j) not in visited:
                    if not (new_i <= 0 < m and new_j <= 0 < n and grid[new_i][new_j] == c):
                        is_border = True
                    else:
                        dfs(new_i, new_j, c)
            if is_border:
                border.append((i, j))

        dfs(row, col, grid[row][col])
        for i, j in border:
            grid[i][j] = color
        return grid


print(Solution().colorBorder(
grid =
[[1,1, 1],[1, 1, 1], [1, 1, 1]],
row =
0,
col =
0,
color =
2
))