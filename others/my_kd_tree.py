import matplotlib.pyplot as plt
import math


class KdNode:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right


class KdTree:
    def __init__(self, points):
        self.root = self.build_tree(points)

    def build_tree(self, points, depth=0):
        if not points:
            return None

        d = len(points[0])
        axis = depth % d

        points = sorted(points, key=lambda x: x[axis])

        median = len(points) // 2

        node = KdNode(points[median],
                      left = self.build_tree(points[:median], depth+1),
                      right = self.build_tree(points[median+1:], depth+1))

        return node

    def search(self, target):
        return self._search(self.root, target)

    def _search(self, node, target, best=None, depth=0):
        if node is None:
            return best

        dist = self.dis(node.point, target)

        if best is None or dist < self.dis(best, target):
            best = node.point

        k = len(node.point)
        axis = depth % k

        if target[axis] < node.point[axis]:
            best = self._search(node.left, target, best, depth+1)
            if dist >= node.point[axis]-target[axis]:  # 画的圆相交了
                best = self._search(node.right, target, best, depth+1)
        else:
            best = self._search(node.right, target, best, depth+1)
            if dist >= target[axis]-node.point[axis]:  # 画的圆相交了
                best = self._search(node.left, target, best, depth+1)
        return best

    def dis(self, cur, target):
        return math.sqrt((cur[0] - target[0]) ** 2 + (cur[1] - target[1]) ** 2)


# 示例使用
points = [
    (2, 3),
    (4, 7),
    (5, 4),
    (9, 6),
    (8, 1),
    (7, 2),
    (3, 9)
]
kd_tree = KdTree(points)
target = (3.1, 7.1)


nearest = kd_tree.search(target)
print(nearest)


for p in points:
    plt.scatter(*p, color="blue")

plt.scatter(*target, color='red')
plt.show()
