"""
给了一个matrix int[][], value代表村庄的海拔，水只能从高处流到低处，给定村庄a和b，
请问在哪里修建水井，水井的海拔最高 对a和b分别作bfs/dfs 看看能到哪些点，都能到的点里面取最高的。
follow up 记得不太清楚了 很确定的是加上了一个cost, 每个格子都有1个cost, 求路径cost最小的点。
用dijkstra, 即使用了优先级队列的bfs. 时间O(MNlg(MN))

我们希望水从某个点出发，能分别“流”到 a 和 b，且路径总成本最小。

步骤如下：
从 a 开始反向建图（只从低向高）跑 Dijkstra

记为 cost_to_a[i][j]：水从某个高点流到 a 的最小代价

从 b 也跑 Dijkstra

记为 cost_to_b[i][j]

对所有格子 (i,j)：

如果这格子能流到 a 和 b（即 cost_to_a[i][j] != inf 且 cost_to_b[i][j] != inf）

计算路径总成本 = cost_to_a[i][j] + cost_to_b[i][j] + cost[i][j]（起点本身也花费）

取总成本最小的 (i,j) 作为井的位置
"""

import heapq
from typing import List, Tuple


class Solution:
    def bestWellWithMinPathCost(self, matrix: List[List[int]], cost: List[List[int]], a: Tuple[int, int],
                                b: Tuple[int, int]) -> Tuple[int, int, int]:
        m, n = len(matrix), len(matrix[0])

        def dijkstra(target: Tuple[int, int]) -> List[List[int]]:
            dist = [[float('inf')] * n for _ in range(m)]
            dist[target[0]][target[1]] = 0
            heap = [(0, target[0], target[1])]

            while heap:
                d, x, y = heapq.heappop(heap)
                if d > dist[x][y]:
                    continue
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        # 只能从低海拔往高海拔走（反向建图）
                        if matrix[nx][ny] >= matrix[x][y]:
                            new_cost = d + cost[x][y]
                            if new_cost < dist[nx][ny]:
                                dist[nx][ny] = new_cost
                                heapq.heappush(heap, (new_cost, nx, ny))
            return dist

        # 从 a 和 b 分别反向跑 Dijkstra
        to_a = dijkstra(a)
        to_b = dijkstra(b)

        # 枚举所有点，找出最小总代价点
        min_total_cost = float('inf')
        best_pos = None
        for i in range(m):
            for j in range(n):
                if to_a[i][j] != float('inf') and to_b[i][j] != float('inf'):
                    total = to_a[i][j] + to_b[i][j] + cost[i][j]
                    if total < min_total_cost:
                        min_total_cost = total
                        best_pos = (i, j)

        return (*best_pos, min_total_cost) if best_pos else None


# 示例调用
matrix = [
    [9, 5, 3],
    [6, 1, 4],
    [7, 2, 8]
]

cost = [
    [3, 8, 6],
    [7, 1, 2],
    [5, 4, 9]
]

a = (1, 1)
b = (2, 2)

sol = Solution()
print(sol.bestWellWithMinPathCost(matrix, cost, a, b))
