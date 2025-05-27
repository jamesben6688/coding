from collections import defaultdict
from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        ans = -1
        visited_time = [0] * n
        cur_time = 1
        for x in range(n):
            start_time = cur_time
            while x != -1 and visited_time[x] == 0:
                visited_time[x] = cur_time
                cur_time += 1
                x = edges[x]

            if x != -1 and visited_time[x] >= start_time:
                ans = max(ans, cur_time-visited_time[x])
        return ans


# class Solution:
#     def longestCycle(self, edges: List[int]) -> int:
#
#         n = len(edges)
#         g = defaultdict(list)
#         for i in range(n):
#             if edges[i] != -1:
#                 g[i].append(edges[i])
#
#         visited = set()
#         ans = -1
#         path = defaultdict()
#
#         def dfs(start, idx):
#             nonlocal ans
#
#             if start in path:
#                 ans = max(ans, len(path) - path[start])
#                 return
#             if start in visited:
#                 return
#             visited.add(start)
#             path[start] = idx
#             for ne in g[start]:
#                 dfs(ne, idx + 1)
#             path.pop(start)
#
#         for i in range(n):
#             dfs(i, 0)
#
#         return ans

print(Solution().longestCycle([2, 0, 1]))