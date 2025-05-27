from typing import *
from collections import defaultdict


class UnionFind:
    def __init__(self, nodes):
        self.father = defaultdict(str)
        self.value = defaultdict(float)
        for n in nodes:
            self.father[n] = n
            self.value[n] = 1.0

    def find(self, x):
        if self.father[x] != x:
            fa = self.father[x]
            self.father[x] = self.find(fa)
            self.value[x] *= self.value(fa)

    def union(self, x, y, w):
        fa_x = self.find(x)
        fa_y = self.find(y)
        if fa_x != fa_y:
            self.father[fa_x] = fa_y
            self.value[fa_x] = self.value[y] * w / self.value[x]
            return True

        return self.value[x] / self.value[y] == w


class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        nodes = set()
        for a, b in equations:
            nodes.add(a)
            nodes.add(b)

        uf = UnionFind(nodes)

        for i, (a, b) in enumerate(equations):
            if not uf.union(a, b, values[i]):
                return False
        return True



print(Solution().checkContradictions(
equations =
[["le","et"],["le","code"],["code","et"]],
values =
[2,5,0.5]
))