"""
我们需要从 (0,0) 出发，到达 (m-1,n-1)，但每次只能进入已经变绿的格子。

关键点：

你不能进入 grid[i][j] > current_time 的格子。

如果你到达某个点太早，就要等到绿灯再进入。
"""

import heapq

def min_time_to_reach(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    heap = [(grid[0][0], 0, 0)]  # (current_time, row, col)

    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    while heap:
        time, x, y = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True

        if x == m - 1 and y == n - 1:
            return time

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                wait_time = max(time + 1, grid[nx][ny])
                heapq.heappush(heap, (wait_time, nx, ny))

    return -1  # unreachable
