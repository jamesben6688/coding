from typing import List

from queue import PriorityQueue


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        left = right = grid[0][0]

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                left = min(left, grid[i][j])
                right = max(right, grid[i][j])

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def check_ok(mid):
            visited = set()

            def dfs(i, j):
                if grid[i][j] > mid:
                    return False
                visited.add((i, j))
                if i == m - 1 and j == n - 1:
                    return grid[i][j] <= mid

                for di, dj in dirs:
                    new_i, new_j = i + di, j + dj
                    if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in visited:
                        if dfs(new_i, new_j):
                            return True
                visited.remove((i, j))
                return False

            return dfs(0, 0)

        while left < right:  # [)
            mid = left + (right - left) // 2
            if check_ok(mid):
                right = mid
            else:
                left = mid + 1
        return left



print(Solution().swimInWater(
[[26,99,80,1,89,86,54,90,47,87],
 [9,59,61,49,14,55,77,3,83,79],
 [42,22,15,5,95,38,74,12,92,71],
 [58,40,64,62,24,85,30,6,96,52],
 [10,70,57,19,44,27,98,16,25,65],
 [13,0,76,32,29,45,28,69,53,41],
 [18,8,21,67,46,36,56,50,51,72],
 [39,78,48,63,68,91,34,4,11,31],
 [97,23,60,17,66,37,43,33,84,35],
 [75,88,82,20,7,73,2,94,93,81]]
))