from collections import defaultdict


class CDOut:
    def output(self, commands):
        g = defaultdict(lambda: defaultdict)

        def get_graph(paths, i):
            if i == len(paths)-1:
                return paths[i]
            else:
                return {paths[i]: get_graph(paths, i+1)}

        def dicMeg(dic1, dic2):
            """嵌套字典合并，参数1旧字典，参数2新字典，结果是将新字典合并到旧字典中"""
            for i in dic2:
                # print(i)
                if i in dic1:
                    if type(dic1[i]) is dict and type(dic2[i]) is dict:
                        dicMeg(dic1[i], dic2[i])
                    else:
                        dic1[i] = [dic1[i], dic2[i]]
                else:
                    dic1[i] = dic2[i]

        def get_path_str(graph, i):
            if isinstance(graph, str):
                if i == 0:
                    return "  " * i + graph + '\n'
                return "  " * i + '-' + graph + '\n'
            elif isinstance(graph, list):
                ans = ""
                for p in graph:
                    if i == 0:
                        ans += '  ' * i + p + '\n'
                    else:
                        ans += '  ' * i + '-' + p + '\n'
                return ans
            else:
                ans = ""
                for k in graph:
                    if i == 0:
                        ans += ' ' * i + k + "\n"
                    else:
                        ans += ' ' * i + '-' + k + "\n"
                    ans += get_path_str(graph[k], i+1)
            return ans

        for c in commands:
            c = c.strip("/")
            paths = c.split("/")
            graph = get_graph(paths, 0)
            dicMeg(g, graph)
            # g.update(graph)

        return get_path_str(g, 0)


print(CDOut().output(
    ["a/b/c",
     "a/e/f",
     "a/b/h",
	 "x/y"
     ]
))


