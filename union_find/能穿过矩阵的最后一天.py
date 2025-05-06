class UnionFind:
    def __init__(self, n):
        self.father = [i for i in range(n)]

    def find(self, x):
        father_x = self.father[x]
        if father_x != x:
            self.father[x] = self.find(father_x)
        return self.father[x]

    def union(self, x, y):
        father_x = self.find(x)
        father_y = self.find(y)
        if father_x != father_y:
            self.father[father_x] = father_y


class Solution:
    def latestDayToCross(self, row: int, col: int, cells) -> int:
        """
            时光倒流法用unionfind
        """
        grid = [[0] * col for _ in range(row)]
        for r, c in cells:
            grid[r-1][c-1] = 1

        # 添加2快超级节点, 连接最上面和最下面
        uf = UnionFind(row * col + 2)
        for i in range(col):
            uf.union(i, row*col)
            uf.union((row-1)*col+i, row*col+1)

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    for di, dj in dirs:
                        ii = i+di
                        jj = j+dj
                        if 0 <= ii < row and 0 <= jj < col and grid[ii][jj] == 0:
                            uf.union(i*col+j, ii*col+jj)

        # 倒流. 每次添加一块陆地
        for i in range(len(cells), 0, -1):
            if uf.find(row * col) == uf.find(row * col + 1):
                return i

            r, c = cells[i-1]
            r -= 1
            c -= 1
            grid[r][c] = 0
            for dr, dc in dirs:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < row and 0 <= cc < col and grid[rr][cc] == 0:
                    # print(r, c, rr, cc)
                    uf.union(r*col+c, rr*col+cc)