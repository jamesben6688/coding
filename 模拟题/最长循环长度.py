from collections import defaultdict
from pprint import pprint

class Solution:
    def get_max_len(self):
        graph = defaultdict(list)
        for i in range(10, 100):
            a = i // 10
            b = i % 10
            nxt = a * b
            cnt = 1
            print(i, nxt)
            while nxt > 1 and nxt < 10:
                b, nxt = nxt, b * nxt
                # b = nxt
                # nxt = b * nxt
                cnt += 1

            graph[i] = [nxt, cnt]

        graph[0] = [0, 0]
        # pprint(graph)

        mx_len = -1
        ans_path = []

        def get_str(path):
            s = ""
            for p, l in path:
                s += str(p)[2-l:]
            return s

        from copy import deepcopy
        def dfs(start, path_len, path):
            nonlocal mx_len, ans_path
            if start in visited:
                s = str(path[0]) + get_str(path[1:-1])
                print(len(s), s)
                if path_len > mx_len:
                    mx_len = max(mx_len, path_len)
                    ans_path = deepcopy(path)
                return
            visited.add(start)
            # try:
            dfs(graph[start][0], path_len+graph[start][1], path+[graph[start]])
            # except:
            #     # print(graph[start][0], path_len+graph[start][1], path+[graph[start]])
            #     raise ValueError("error")
            visited.remove(start)

        for i in range(10, 100):
            visited = set()
            # visited.add(i)
            print(i, end=" ")
            dfs(i, 2, [i])

        print(mx_len, ans_path, str(ans_path[0]) + get_str(ans_path[1:]))
        print(get_str(ans_path[1:]))


Solution().get_max_len()