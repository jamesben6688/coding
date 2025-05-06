class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius


from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.fathers = [x for x in range(n)]
        self.cnt = n

    def find(self, x):
        if self.fathers[x] != x:
            self.fathers[x] = self.find(self.fathers[x])
        return self.fathers[x]

    def union(self, x, y):
        father_x = self.find(x)
        father_y = self.find(y)
        if father_x != father_y:
            self.fathers[father_x] = father_y
            self.cnt -= 1


class Solution:
    def is_one_group(self, circles):
        # graph = defaultdict(list)

        n = len(circles)
        uf = UnionFind(n)
        def l2_distance_squre(circle_1, circle_2):
            return (circle_1.center_x - circle_2.center_x) ** 2 + (circle_1.center_y - circle_2.center_y) ** 2
        for i in range(n):
            for j in range(i+1, n):
                if l2_distance_squre(circles[i], circles[j]) <= (circles[i].radius + circles[j].radius) ** 2:
                    uf.union(i, j)

        return uf.cnt



print(Solution().is_one_group(
    # [Circle(0, 0, 3), Circle(4, 0, 3), Circle(2, 3, 2)],
    # [Circle(0, 0, 5), Circle(0, 0, 3)],  # 期望输出: 同一组
    [Circle(0, 0, 3), Circle(4, 0, 3),
     Circle(2, 3, 2), Circle(10, 10, 1)],  # 期望输出: 前三个同一组，第四个不同组
))