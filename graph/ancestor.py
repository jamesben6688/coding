from typing import List
from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        indegrees = [0] * n
        for a, b in edges:
            g[a].append(b)
            indegrees[b] += 1

        que = deque()
        ans = [set() for _ in range(n)]
        for x in range(n):  # indegrees:
            if indegrees[x] == 0:
                que.append(x)

        while que:
            q_size = len(que)
            for i in range(q_size):
                cur = que.popleft()
                for ne in g[cur]:
                    ans[ne].add(cur)
                    ans[ne] = ans[ne].union(ans[cur])
                    indegrees[ne] -= 1
                    if indegrees[ne] == 0:
                        que.append(ne)
        return [list(x) for x in ans]


print(Solution().getAncestors(6, [[0,3],[5,0],[2,3],[4,3],[5,3],[1,3],[2,5],[0,1],[4,5],[4,2],[4,0],[2,1],[5,1]]))