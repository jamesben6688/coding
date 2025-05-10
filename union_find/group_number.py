class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


def can_reach_union_find(nums, a, b):
    uf = UnionFind()

    for num in nums:
        for digit in set(str(num)):
            uf.union(num, f'digit_{digit}')  # Union number with its digits

    return uf.find(a) == uf.find(b)
