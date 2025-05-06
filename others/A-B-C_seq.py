from collections import defaultdict


class Solution:

    def has_path(self, edges):
        graph = defaultdict(list)
        visited = defaultdict(bool)
        path = []
        ans = []
        cnt = defaultdict(int)
        for s, t in edges:
            graph[s].append(t)
            if 'A' in s and 'B' in t:
                cnt[t] += 1
            visited[s] = False
            visited[t] = False

        def dfs(cur):
            nonlocal path, ans
            if 'C' in cur:
                ans.append(path[:])
                return True

            if visited[cur]: return False

            visited[cur] = True
            if 'A' in cur:
                for ne in graph[cur]:
                    if 'B' in ne and cnt[ne] >= 2:
                        path.append(ne)
                        dfs(ne)
                        # if dfs(ne): return True
                        path.pop()

            if 'B' in cur:
                for ne in graph[cur]:
                    if 'B' in ne and cnt[ne] >= 2 or 'C' in ne:
                        path.append(ne)
                        dfs(ne)
                        # if dfs(ne): return True
                        path.pop()
            visited[cur] = False
            return False

        for k in graph:
            if 'A' in k:
                path.append(k)
                dfs(k)
                # if dfs(k):
                #     print(ans)
                    # return True
                path.pop()
        print(ans)
        return False


edges = [
    ['A1', 'B1'],
    ['A1', 'B2'],
    ['A3', 'B1'],
    ['B1', 'C1'],
    ['B2', 'C2']
]

print(Solution().has_path(edges))
