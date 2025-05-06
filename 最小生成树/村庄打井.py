from typing import List


class UnionFind:
    def __init__(self, n):
        self.father = [x for x in range(n)]

    def find(self, x):
        if self.father[x] != x:
            self.father[x] = self.find(self.father[x])

        return self.father[x]

    def union(self, x, y):
        father_x = self.find(x)
        father_y = self.find(y)
        if father_x != father_y:
            self.father[father_x] = father_y
            return True
        return False

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        for i in range(n):
            pipes.append([i, n, wells[i]])

        pipes = sorted(pipes, key=lambda x: x[2])
        
        uf = UnionFind(n+1)
        cnt = 0
        cost = 0
        for a, b, c in pipes:
            if uf.union(a, b):
                cost += c
                cnt += 1
            if cnt == n:
                return cost
        return -1


print(Solution().minCostToSupplyWater(
n =
5,
wells =
[46012,72474,64965,751,33304],
pipes =
[[2,1,6719],[3,2,75312],[5,3,44918]]
))