"""
    可撤销的并查集里面, 不能使用路径压缩。可以使用size压缩

"""
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.father = [x for x in range(n)]
        self.size = [1 for _ in range(n)]
        self.history = defaultdict(list)

    def find(self, x):
        if self.father[x] != x:
            return self.find(self.father[x])

        return self.father[x]

    def union(self, x, y):
        father_x = self.find(x)
        father_y = self.find(y)
        if father_x == father_y:
            return
        self.history[(x, y)] = [father_x, father_y, self.size[father_x], self.size[father_y]]
        if self.size[father_x] > self.size[father_y]:
            father_x, father_y = father_y, father_x

        self.father[father_x] = father_y
        self.size[father_y] += self.size[father_x]

    def undo(self, x, y):
        old_father_x, old_father_y = self.history[(x, y)]
        self.father[old_father_x] = old_father_x
        self.size[old_father_y] -= self.size[old_father_x]



