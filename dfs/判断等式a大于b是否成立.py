from collections import defaultdict


class Solution:
    def is_valid(self, ineqs):
        graph = defaultdict(dict)
        def dfs(cur, visited, path_weights):
            if cur in visited:
                return True, path_weights[:]
            visited.add(cur)
            for nei, wt in graph[cur].items():
                if nei not in visited:
                    path_weights.append(wt)

                    if dfs(nei, visited, path_weights)[0]:
                        return True, path_weights[:]
                    path_weights.pop()
                else:
                    path_weights.append(wt)
                    return True, path_weights[:]
            visited.remove(cur)
            return False, path_weights[:]

        for eq in ineqs:
            eq = eq.replace(" ", "")
            a = eq[0]
            b = eq[-1]
            op = eq[1:-1]

            # insert new edge
            if op == "<":
                graph[a][b] = 0
            elif op == "<=":
                graph[a][b] = 1
            elif op == ">":
                graph[b][a] = 0
            elif op == ">=":
                graph[b][a] = 1

            # check if adding this edge introduces invalid cycle
            visited = set()
            path_weights = []
            if op == "<":
                has_circyle, path = dfs(a, visited, path_weights)
                if has_circyle:
                    print("invalid")
                else:
                    print('valid')
            elif op == "<=":
                has_circyle_1, path_1 = dfs(a, visited, [])
                visited.clear()
                has_circyle_2, path_2 = dfs(b, visited, [])
                if not has_circyle_1:
                    print("valid")
                elif has_circyle_2 and 0 not in path_2:
                    print('valid')
                else:
                    print('invalid')
            elif op == ">":
                has_circyle, path = dfs(b, visited, path_weights)
                if has_circyle:
                    print("invalid")
                else:
                    print('valid')
            else:
                has_circyle_1, path_1 = dfs(b, visited, [])
                visited.clear()
                has_circyle_2, path_2 = dfs(a, visited, [])
                if not has_circyle_1:
                    print("valid")
                elif has_circyle_2 and 0 not in path_2:
                    print('valid')
                else:
                    print('invalid')


Solution().is_valid(["a <= b", "b < c", "d <= e", "e <= f", "f <= d", "g < h", "h <= g"])  # valid
