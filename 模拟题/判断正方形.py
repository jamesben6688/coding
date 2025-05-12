"""
要求拆解：
基本功能：

能够动态加点 add_point(x, y)

能够实时找出所有有效的正方形

Follow-up 功能：

允许存在一个误差范围 epsilon，两个边长度差在这个范围内仍然算正方形

✅ 思路：
1. 存储结构
使用 set 存储所有点，方便 O(1) 查询是否存在某个点。

2. 正方形判断方法
遍历所有点对 (p1, p2)，当它们可以构成一个正方形的对角线时，我们就能确定另外两个点的位置 (p3, p4)。

然后检查 p3, p4 是否也在点集中。

3. 判断是否为正方形（带误差）
检查 4 边长度是否相等（或在误差范围 epsilon 内）

检查对角线是否相等（或在误差范围内）
"""

import matplotlib.pyplot as plt
from typing import List
from math import isclose


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(a, b):
                return (a[0] - b[0])**2 + (a[1] - b[1])**2

        d = sorted([
            dist(p1, p2),
            dist(p1, p3),
            dist(p1, p4),
            dist(p2, p3),
            dist(p2, p4),
            dist(p3, p4),
        ])
        if d[0] == 0: return False
        self.epsilon = 1e-6
        # Square must have 4 equal sides, 2 equal diagonals
        side = d[0]
        return (
            isclose(d[0], side, abs_tol=self.epsilon) and
            isclose(d[1], side, abs_tol=self.epsilon) and
            isclose(d[2], side, abs_tol=self.epsilon) and
            isclose(d[3], side, abs_tol=self.epsilon) and
            isclose(d[4], 2 * side, abs_tol=self.epsilon) and
            isclose(d[5], 2 * side, abs_tol=self.epsilon)  # diagonal: 2 * side^2
        )

class ValidSquares:
    def __init__(self):
        # 存储所有点的集合
        self.points_set = set()
        # 存储找到的所有正方形的集合 (为了避免重复)
        self.squares = set()

    def add_point(self, x, y):
        """
        向集合中添加一个新的点，检查是否能形成正方形。
        """
        self.points_set.add((x, y))
        self._find_squares(x, y)

    # 不停加点, 当前点+另外一点构成对角线O(N)
    def _find_squares(self, x, y):
        """
        查找所有有效的正方形。
        通过新加入的点 (x, y)，检查它与其他点的组合是否能形成正方形。
        """
        for (px, py) in list(self.points_set):
            if (px, py) == (x, y):  # 不用跟自己匹配
                continue

            # 计算与 (px, py) 形成对角线的其他两点
            dx, dy = x - px, y - py
            # 找到两个其他的点的位置：向上右转和向下左转
            point1 = (x + dy, y - dx)
            point2 = (px + dy, py - dx)

            # 如果这两个点都在集合中，说明构成了一个正方形
            if point1 in self.points_set and point2 in self.points_set:
                # 将这个正方形添加到集合中，保证不会重复
                sorted_square = tuple(sorted([(x, y), (px, py), point1, point2]))
                self.squares.add(sorted_square)

    def get_squares(self):
        """
        返回所有找到的正方形。
        """
        return list(self.squares)

# 示例使用
valid_squares = ValidSquares()
valid_squares.add_point(1, 1)
valid_squares.add_point(1, 2)
valid_squares.add_point(2, 1)
valid_squares.add_point(2, 2)

# 输出所有找到的正方形
squares = valid_squares.get_squares()
print("Valid squares:", squares)



print(Solution().validSquare(
p1 =
[6987,-473],
p2 =
[6985,-473],
p3 =
[6986,-472],
p4 =
[6986,-474]
))