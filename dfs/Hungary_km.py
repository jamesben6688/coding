from typing import List
import sys

INF = 1 << 60

class KM:
    def __init__(self, n):
        self.n = n
        self.w = [[-INF] * (n + 1) for _ in range(n + 1)]
        self.la = [0] * (n + 1)
        self.lb = [0] * (n + 1)
        self.match = [0] * (n + 1)
        self.va = [0] * (n + 1)
        self.vb = [0] * (n + 1)
        self.d = [INF] * (n + 1)

    def add_edge(self, u, v, weight):
        self.w[u][v] = weight

    def dfs(self, x):
        self.va[x] = 1
        for y in range(1, self.n + 1):
            if not self.vb[y]:
                gap = self.la[x] + self.lb[y] - self.w[x][y]
                if gap == 0:
                    self.vb[y] = 1
                    if not self.match[y] or self.dfs(self.match[y]):
                        self.match[y] = x
                        return True
                else:
                    self.d[y] = min(self.d[y], gap)
        return False

    def run(self):
        # 初始化左顶标为每个点最大边权
        for i in range(1, self.n + 1):
            self.la[i] = max(self.w[i][1:])
        # 主循环
        for i in range(1, self.n + 1):
            self.d = [INF] * (self.n + 1)
            while True:
                self.va = [0] * (self.n + 1)
                self.vb = [0] * (self.n + 1)
                if self.dfs(i):
                    break
                delta = INF
                for j in range(1, self.n + 1):
                    if not self.vb[j]:
                        delta = min(delta, self.d[j])
                for j in range(1, self.n + 1):
                    if self.va[j]:
                        self.la[j] -= delta
                    if self.vb[j]:
                        self.lb[j] += delta
        # 求最大权
        res = 0
        for i in range(1, self.n + 1):
            res += self.w[self.match[i]][i]
        return res, self.match[1:]  # match[1] 匹配右边第 1 个点的左点


# Example usage:
# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     km = KM(n)
#     for _ in range(m):
#         u, v, w = map(int, input().split())
#         km.add_edge(u, v, w)
#     total_weight, matching = km.run()
#     print(total_weight)
#     print(" ".join(map(str, matching)))
