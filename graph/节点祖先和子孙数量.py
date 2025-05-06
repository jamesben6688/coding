from collections import defaultdict


class Solution:
    def ance_dece(self, edges, n):
        graph = defaultdict(list)
        indegrees = [0 for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            indegrees[b] += 1

        ance = defaultdict(int)
        dece = defaultdict(set)  # bit mainulation   int
        path = []

        def dfs(root):
            nonlocal path
            for x in path:
                dece[x].add(root)  # 3   dece[x] or 1 << 3
            ance[root] += len(path)
            for ne in graph[root]:
                path.append(root)
                dfs(ne)
                path.pop()

        for x in range(n):
            if indegrees[x] == 0:
                dfs(x)

        return ance, dece


print(Solution().ance_dece(
    [
        [0, 3],
        [1, 2],
        [2, 3]
    ], 4
))
