class UnionFind:
    def __init__(self, n):
        self.father = [i for i in range(n)]
        self.cnt = 0

    def find(self, x):
        if self.father[x] != x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, x, y):
        father_x = self.find(x)
        father_y = self.find(y)

        if father_x != father_y:
            self.father[father_x] = father_y
            self.cnt -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ans = []
        grid = [[0 for i in range(n)] for j in range(m)]

        uf = UnionFind(m * n)

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for r, c in positions:
            if grid[r][c] == 1:
                ans.append(uf.cnt)
                continue
            uf.cnt += 1
            grid[r][c] = 1
            for d in dirs:
                rr = r + d[0]
                cc = c + d[1]

                if 0 <= rr < m and 0 <= cc < n and grid[rr][cc] == 1 and uf.father[rr * n + cc] != uf.father[r * n + c]:
                    uf.union(rr * n + cc, r * n + c)

            ans.append(uf.cnt)
        return ans
