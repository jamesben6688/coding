import random
from collections import defaultdict, deque
from heapq import *


class Solution:
    def top_k_similar_pair(self, videos, edges, k):
        n = len(videos)
        graph = defaultdict(defaultdict)
        for i, j, s in edges:
            graph[i].update({j: s})
            graph[j].update({i: s})

        ans = []
        added = set()
        for v in videos:
            que = []
            heappush(que, (-1, v))
            # que.append(v)
            visited = set()
            visited.add(v)
            sim = {x: [0, []] for x in videos}
            sim[v] = [1, [v]]
            while que:
                s, x = heappop(que)
                s = -s
                visited.add(x)
                if x != v:
                    # ans.append((s, v, x))
                    if v+x not in added:
                        heappush(ans, (s, v, x))
                        added.add(v+x)
                        added.add(x+v)
                    if len(ans) > k:
                        heappop(ans)
                for ne in graph[x]:
                    if ne not in visited and graph[x][ne] * s > sim[ne][0]:
                        sim[ne][0] = graph[x][ne] * s
                        sim[ne][1] = sim[x][1] + [ne]
                        heappush(que, (-sim[ne][0], ne))
            print(v, sim)
        return sorted(ans, reverse=True)




videos = ['A', 'B', 'C', 'D', 'E']

# 随机生成视频之间的边和相似度（边的权重）
# edges = [
#     ('A', 'B', random.uniform(0.1, 0.9)),
#     ('B', 'C', random.uniform(0.1, 0.9)),
#     ('A', 'C', random.uniform(0.1, 0.9)),
#     ('A', 'D', random.uniform(0.1, 0.9)),
#     ('D', 'E', random.uniform(0.1, 0.9)),
#     ('B', 'D', random.uniform(0.1, 0.9)),
#     ('C', 'E', random.uniform(0.1, 0.9)),
# ]

edges = [
    ('A', 'B', 0.33867226227162095),
    ('B', 'C', 0.34360356636396683),
    ('A', 'C', 0.5743097086426759),
    ('A', 'D', 0.24451056675643512),
    ('D', 'E', 0.4516762261475651),
    ('B', 'D', 0.14118118101300095),
    ('C', 'E', 0.7648222463034106)
]

# print(edges)

print(Solution().top_k_similar_pair(videos, edges, 10))
