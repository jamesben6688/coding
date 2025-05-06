from collections import defaultdict
from heapq import *



class Solution:
    def shortest_path(self, n, edges, start, end):
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        visited = [False for _ in range(n)]
        visited[start] = True
        dis = [[float('inf'), ""] for _ in range(n)]
        dis[start] = [0, f"{start}"]
        que = [(0, start)]

        while que:
            cur_dis, cur = heappop(que)
            if cur == end:
                return dis[cur]
            visited[cur] = True
            for ne in graph[cur]:
                if not visited[ne] and cur_dis + 1 < dis[ne][0]:
                    # dis[ne] = cur_dis + ne
                    dis[ne] = [cur_dis+1, dis[cur][1]+str(ne)]
                    heappush(que, (dis[ne][0], ne))
        return ""

edges=[
    (0, 1),
    (0, 2),
    (1, 0),
    (1, 3),
    (2, 0),
    (2, 3),
    (3, 1),
    (3, 2),
    (3, 4),
    (4, 3)
]
n=5
start = 0
end = 4
print(Solution().shortest_path(n, edges, start, end))
