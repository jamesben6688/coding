# from heapq import *
# from collections import Counter
#
#
# class Solution:
#     def build_graph(self, codes):
#         """
#         使用1个heap保存所有degree为1的节点
#         degree使用Counter保存所有的度
#             the nodes are: 1-n
#
#         时间复杂度: O(nlg(N))
#         :param n:
#         :param codes:
#         :return:
#         """
#         n = len(codes) + 3
#         degree = Counter({x: 1 for x in range(n)})
#         degree.pop(0)
#         heap = [x for x in degree if degree[x] == 1]
#         edges = []
#         for code in codes:
#             leaf = heappop(heap)
#             edges.append([leaf, code])
#             degree[code] -= 1
#             if degree[code] == 1:
#                 heappush(heap, code)
#         edges.append([heappop(heap), heappop(heap)])
#         return edges

from typing import List, Tuple

def prufer_decode(code: List[int]) -> List[Tuple[int, int]]:
    n = len(code) + 2
    degree = [1] * n
    for v in code:
        degree[v] += 1

    ptr = 0
    while degree[ptr] != 1:
        ptr += 1
    leaf = ptr

    edges = []
    for v in code:
        edges.append((leaf, v))
        degree[leaf] -= 1
        degree[v] -= 1

        if degree[v] == 1 and v < ptr:
            """
                新产生的叶节点需要更小, 使用新的
            """
            leaf = v
        else:
            """
                继续找下一个最小的叶节点
            """
            ptr += 1
            while ptr < n and degree[ptr] != 1:
                ptr += 1
            leaf = ptr

    # 最后一条边
    u, v = [i for i in range(n) if degree[i] == 1]
    edges.append((u, v))
    return edges


print(prufer_decode([4, 4, 5, 6, 5]))
# print(Solution().build_graph([5, 5, 6, 7, 6]))
