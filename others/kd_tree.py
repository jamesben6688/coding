import math


class KdNode:
    def __init__(self, point, left=None, right=None):
        self.point = point  # 存储的点
        self.left = left  # 左子树
        self.right = right  # 右子树


class KdTree:
    def __init__(self, points):
        self.root = self.build_tree(points, depth=0)

    def build_tree(self, points, depth):
        if not points:
            return None

        # 选择划分维度，循环使用
        k = len(points[0])  # 假设所有点有相同的维度
        axis = depth % k  # 使用当前深度决定维度

        # 按照当前维度对点进行排序
        points.sort(key=lambda x: x[axis])

        # 找到中位数
        median = len(points) // 2

        # 创建当前节点
        node = KdNode(
            point=points[median],
            left=self.build_tree(points[:median], depth + 1),
            right=self.build_tree(points[median + 1:], depth + 1)
        )

        return node

    def nearest_neighbor(self, target):
        return self._nearest_neighbor(self.root, target, depth=0, best=None)

    def _nearest_neighbor(self, node, target, depth, best):
        if node is None:
            return best

        # 计算当前节点到目标点的距离
        dist = self._distance(node.point, target)

        # 更新最佳点
        if best is None or dist < self._distance(best, target):
            best = node.point

        # 当前轴
        k = len(target)
        axis = depth % k

        # 比较目标点与当前节点的值，决定搜索哪边的子树
        if target[axis] < node.point[axis]:
            best = self._nearest_neighbor(node.left, target, depth + 1, best)
            # 如果可能存在更好的点在右子树中，考虑右子树
            if target[axis] + dist >= node.point[axis]:
                best = self._nearest_neighbor(node.right, target, depth + 1, best)
        else:
            best = self._nearest_neighbor(node.right, target, depth + 1, best)
            # 如果可能存在更好的点在左子树中，考虑左子树
            if target[axis] - dist <= node.point[axis]:
                best = self._nearest_neighbor(node.left, target, depth + 1, best)

        return best

    def _distance(self, point1, point2):
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))


# 示例使用
# points = [
#     (2, 3),
#     (4, 7),
#     (5, 4),
#     (9, 6),
#     (8, 1),
#     (7, 2),
#     (3, 9)
# ]

points = [
    (1, 1),
    (2, 7),
    (3, 1),
    (4, 1)
]

# 创建 k-d 树
kd_tree = KdTree(points)

# 查询最近邻
# target = (6, 5)
target = (3.1, 7.1)
nearest = kd_tree.nearest_neighbor(target)
print(f"Nearest neighbor to {target} is {nearest}")

# import math
#
#
# class KdNode:
#     def __init__(self, point, left=None, right=None):
#         self.point = point
#         self.left = left
#         self.right = right
#
#
# class KdTree:
#     def __init__(self, points):
#         self.root = self.build_tree(points, depth=0)
#
#     def build_tree(self, points, depth):
#         if not points:
#             return None
#
#         k = len(points[0])
#         axis = depth % k
#
#         points.sort(key=lambda x: x[axis])
#
#         median = len(points) // 2
#
#         node = KdNode(
#             point = points[median],
#             left = self.build_tree(points[:median], depth+1),
#             right=self.build_tree(points[median+1:], depth+1)
#         )
#
#         return node
#
#     def nearest_neighbor(self, target):
#         return self._nearest_neighbor(self.root, target, depth=0, best=None)
#
#     def _nearest_neighbor(self, node, target, depth, best):
#         if node is None:
#             return best
#
#         dist = self._distance(node.point, target)
#
#         k = len(target)
#         axis = depth % k
#
#         # 比较目标点与当前节点的值，决定搜索哪边的子树
#         if target[axis] < node.point[axis]:
#             best = self._nearest_neighbor(node.left, target, depth + 1, best)
#             # 如果可能存在更好的点在右子树中，考虑右子树
#             if target[axis] + dist >= node.point[axis]:
#                 best = self._nearest_neighbor(node.right, target, depth + 1, best)
#         else:
#             best = self._nearest_neighbor(node.right, target, depth + 1, best)
#             # 如果可能存在更好的点在左子树中，考虑左子树
#             if target[axis] - dist <= node.point[axis]:
#                 best = self._nearest_neighbor(node.left, target, depth + 1, best)
#
#         return best
#
#     def _distance(self, point1, point2):
#         return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))
#
# # 示例使用
# points = [
#     (2, 3),
#     (4, 7),
#     (5, 4),
#     (9, 6),
#     (8, 1),
#     (7, 2),
#     (3, 9)
# ]
#
# # 创建 k-d 树
# kd_tree = KdTree(points)
#
# # 查询最近邻
# target = (6, 5)
# nearest = kd_tree.nearest_neighbor(target)
# print(f"Nearest neighbor to {target} is {nearest}")
