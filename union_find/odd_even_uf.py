class UnionFind:
    def __init__(self):
        self.parent = {}
        self.diff = {}  # 记录x到root有多少个1, 也就是奇偶性

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.diff[x] = 0
            return x
        if self.parent[x] != x:
            orig_parent = self.parent[x]
            root = self.find(orig_parent)
            self.diff[x] ^= self.diff[orig_parent]
            self.parent[x] = root
        return self.parent[x]

    def union(self, x, y, parity):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            # check consistency
            return (self.diff[x] ^ self.diff[y]) == parity

        self.parent[rx] = ry
        self.diff[rx] = self.diff[x] ^ self.diff[y] ^ parity
        return True
uf = UnionFind()


def add_constraint(start, end, parity_str):
    parity = 1 if parity_str == 'odd' else 0  # 注意constraint里面不能调换
    # we work with S[start] and S[end+1]
    return uf.union(start, end + 1, parity)


print(add_constraint(1, 1, 'odd'))   # True
print(add_constraint(2, 3, 'even'))  # True
print(add_constraint(1, 3, 'even'))  # False