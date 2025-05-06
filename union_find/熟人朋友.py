"""

1101
Unfriend动作，
撤销好友关系，那么最早时间所有人都成为朋友会如何变

可以用一个history保存之前的root

class UnionFindUndo:
    def __init__(self, n):
        self.parent = list(range(n))
        self.history = []  # 保存 (x, y, parent_y, count) 的记录
        self.count = n

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            self.history.append((x, y, None))  # 无效合并也记录
            return
        self.parent[root_y] = root_x
        self.count -= 1
        self.history.append((x, y, root_y))  # 保存被更改的 y 的 root

    def undo(self, x, y):
        if not self.history:
            return
        # 从历史中找到最近一次 x 和 y 的 union 记录
        for i in range(len(self.history) - 1, -1, -1):
            hx, hy, root_y = self.history[i]
            if (hx == x and hy == y) or (hx == y and hy == x):
                self.history.pop(i)
                if root_y is not None:
                    self.parent[root_y] = root_y
                    self.count += 1
                break  # 一次 undo 完成


"""

class UnionFind:
    def __init__(self, n):
        self.father = [x for x in range(n)]
        self.n = n

    def find(self, x):
        if self.father[x] != x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, x, y):
        father_x = self.find(x)
        father_y = self.find(y)
        if father_x != father_y:
            self.father[father_x] = father_y
            self.n -= 1


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs = sorted(logs, key=lambda x: x[0])
        uf = UnionFind(n)
        for t, a, b in logs:
            uf.union(a, b)
            # print(uf.n)
            if uf.n == 1:
                return t

        return -1