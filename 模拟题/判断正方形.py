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
    def validSquare_1(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # if
        def get_center(p1, p2, p3, p4):
            # print(p1[0])
            return [(p1[0]+p2[0]+p3[0]+p4[0])/4, (p1[1]+p2[1]+p3[1]+p4[1])/4]

        center = get_center(p1, p2, p3, p4)

        def l2_dis(p1, p2):
            return (p1[0]-p2[0]) **2 + (p1[1]-p2[1]) ** 2

        dis = l2_dis(center, p1)
        if dis != l2_dis(center, p2) or dis != l2_dis(center, p3) or dis != l2_dis(center, p3):
            return False

        pts = [p1, p2, p3, p4]
        for i in range(4):
            for j in range(i+1, 4):
                pp1 = pts[i]
                pp2 = pts[j]

                if pp1 == pp2: return False

                vec1 = [pp1[0]-center[0], pp1[1]-center[1]]
                vec2 = [pp2[0]-center[0], pp2[1]-center[1]]

                if vec1[0] * vec2[0] + vec1[1]*vec2[1] == 0:
                    pass
                elif vec1[0]+vec2[0] == 0 and vec1[1]+vec2[1] ==0:
                    pass
                else:
                    return False
            return True


class Solution_1:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def get_center(p1, p2, p3, p4):
            print(p1[0])
            return [(p1[0]+p2[0]+p3[0]+p4[0])/4, (p1[1]+p2[1]+p3[1]+p4[1])/4]

        center = get_center(p1, p2, p3, p4)

        def l2_dis(p1, p2):
            return (p1[0]-p2[0]) ** 2 + (p1[1]-p2[1])**2

        dis = l2_dis(center, p1)
        if dis != l2_dis(center, p2) or dis != l2_dis(center, p3) or dis != l2_dis(center, p3):
            return False

        pts = [p1, p2, p3, p4]

        plt.scatter(*p1, label='pt1')
        plt.scatter(*p2, label='pt2')
        plt.scatter(*p3, label='pt3')
        plt.scatter(*p4, label='pt4')
        plt.scatter(*center, label='center')

        plt.legend()
        plt.show()

        for i in range(4):
            for j in range(i+1, 4):
                pp1 = pts[i]
                pp2 = pts[j]

                vec1 = [pp1[0]-center[0], pp1[1]-center[1]]
                vec2 = [pp2[0]-center[0], pp2[1]-center[1]]

                if vec1[0] * vec2[0] + vec1[1]*vec2[1] == 0:
                    pass
                elif vec1[0]+vec2[0] == 0 and vec1[1]+vec2[1] ==0:
                    pass
                else:
                    return False
            return True


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