"""
    可以先用flood fill找出candidate, 减少bfs的次数

"""
from collections import deque

def find_best_service_spot(grid):
    rows, cols = len(grid), len(grid[0])
    dist_sum = [[0]*cols for _ in range(rows)]
    reach_count = [[0]*cols for _ in range(rows)]
    total_customers = 0

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    def bfs(start_r, start_c):
        visited = [[False]*cols for _ in range(rows)]
        queue = deque([(start_r, start_c, 0)])
        visited[start_r][start_c] = True

        while queue:
            r, c, d = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    if grid[nr][nc] == '.':
                        dist_sum[nr][nc] += d + 1
                        reach_count[nr][nc] += 1
                        queue.append((nr, nc, d + 1))
                        visited[nr][nc] = True

    # Step 1: locate all customer tables
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'C':
                total_customers += 1
                bfs(r, c)

    # Step 2: Find best empty cell
    min_distance = float('inf')
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and reach_count[r][c] == total_customers:
                min_distance = min(min_distance, dist_sum[r][c])

    return min_distance if min_distance != float('inf') else -1
