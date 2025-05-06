"""
You are given a map with 2 colors of lands - red and blue. The map looks like below where R represents a land of red,
B represents a land of blue and . represents the sea.
We want to build a bridge between blue and red lands at minimum cost. The cost of a bridge is proportional to its length.
Write a function to return the shortest distance between the two lands.
Please note that the bridge must be connected in 4-directions; up, right, down and left.
Example 1:
[input]
.RR...
R....B
R....B
RR....
[output]
3
Example 2:
[input]
.RB...
R....B
..B...
R.....
[output]
0

面试官要求bridge不能拐弯比如先向下再向右这种是不允许的

类似 934.

本题思路
"""

from typing import List
from collections import deque

def shortest_bridge_dir(grid: List[str]) -> int:
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # 上下左右

    min_result = float('inf')

    for dr, dc in directions:
        queue = deque()
        visited = [[False]*cols for _ in range(rows)]

        # Step 1: 找到边界红色点往 dr,dc 是海的位置
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'R':
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 'B': return 0

                        if grid[nr][nc] == '.':
                            queue.append((nr, nc, 1))  # 海起点
                            visited[nr][nc] = True

        # Step 2: BFS 只能往 dr,dc 方向走，但检查 4 向终点
        while queue:
            r, c, dist = queue.popleft()

            # ✅ 在当前位置四个方向看是否是 B
            for adj_dr, adj_dc in directions:
                adj_r, adj_c = r + adj_dr, c + adj_dc
                if 0 <= adj_r < rows and 0 <= adj_c < cols:
                    if grid[adj_r][adj_c] == 'B':
                        min_result = min(min_result, dist)
                        queue.clear()
                        break  # 提前终止当前方向的搜索

            # ⏩ 继续往原方向走
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                if grid[nr][nc] == '.':
                    queue.append((nr, nc, dist + 1))
                    visited[nr][nc] = True

    return min_result if min_result != float('inf') else -1


grid1 = [
    ".RR...",
    "R....B",
    "R....B",
    "RR...."
]
print(shortest_bridge_dir(grid1))  # 3

grid2 = [
    ".RB...",
    "R....B",
    "..B...",
    "R....."
]
print(shortest_bridge_dir(grid2))  # 0
