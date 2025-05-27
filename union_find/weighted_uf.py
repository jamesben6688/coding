class UnionFind:
    def __init__(self, n):
        self.father = [x for x in range(n)]
        self.dis = [0 for x in range(n)]

    def find(self, x):
        if self.father[x] != x:
            tmp = self.father[x]
            self.father[x] =  self.find(tmp)
            self.dis[x] += self.dis[tmp]

        return self.father[x]

    def union(self, x, y, w):
        father_x = self.find(x)
        father_y = self.find(y)

        if father_x != father_y:
            self.father[father_x] = father_y
            self.dis[father_x] = w+self.dis[y]-self.dis[x]

            return True

        return False


uf = UnionFind(n)