import itertools


"""
图同构例子
图1：

Copy
Edit
1 - 2
|   |
3 - 4
图2：

Copy
Edit
10 - 11
|     |
12 - 13
这两个图是同构的：只要你建立一个映射 1→10, 2→11, 3→12, 4→13 就能完全一一对应。

✅ 解法
图同构问题是经典的 NP问题，不过对 小图（比如节点数 < 10~20）可以暴力尝试所有可能的映射。
"""
def is_isomorphic(g1, g2):
    if len(g1) != len(g2):
        return False

    nodes1 = list(g1.keys())
    nodes2 = list(g2.keys())

    for perm in itertools.permutations(nodes2):
        mapping = dict(zip(nodes1, perm))

        match = True
        for u in nodes1:
            mapped_u = mapping[u]
            mapped_neighbors = set(mapping[v] for v in g1[u])
            if set(g2[mapped_u]) != mapped_neighbors:
                match = False
                break
        if match:
            return True

    return False

