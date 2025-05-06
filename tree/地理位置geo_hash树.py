"""
类似于GeoHash，给定两个数据结构Node表示GeoHash的一个位置，他可以有四个children，表示他分成四份，或者他只有一个Point表示一个饭店
 Node 和 Point这两个类都有getDistance方法，来计算他们到某一个Point的距离，对于Node 就是表示Point到他的四条边的最短距离
 需要实现的是给定GeoHash的root，和一个Point表示一个人当前的位置，如何返回下一个离他最近的饭店。

 Node可以看成是一个QuadTree之类的
"""
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def getDistance(self, other: 'Point') -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

class Node:
    def __init__(self, min_x, max_x, min_y, max_y):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.children = []  # Can be Points or Nodes

    def getDistance_l2(self, point: Point) -> float:
        dx = 0
        if point.x < self.min_x:
            dx = self.min_x - point.x
        elif point.x > self.max_x:
            dx = point.x - self.max_x

        dy = 0
        if point.y < self.min_y:
            dy = self.min_y - point.y
        elif point.y > self.max_y:
            dy = point.y - self.max_y

        return (dx ** 2 + dy ** 2) ** 0.5

    def getDistance(self, point: 'Point') -> float:
        d_left = abs(point.x - self.min_x)
        d_right = abs(point.x - self.max_x)
        d_bottom = abs(point.y - self.min_y)
        d_top = abs(point.y - self.max_y)
        return min(d_left, d_right, d_top, d_bottom)




import heapq

def findNearestRestaurant(root: 'Node', current: 'Point') -> ['Point', None]:
    # 每个元素是 (distance, unique_id, obj)，其中 obj 可以是 Node 或 Point
    heap = []
    uid = 0  # 避免 heap 比较 Node 对象报错

    def push(obj):
        nonlocal uid
        dist = obj.getDistance(current)
        heapq.heappush(heap, (dist, uid, obj))
        uid += 1

    push(root)

    while heap:
        dist, _, obj = heapq.heappop(heap)

        if isinstance(obj, Point):
            return obj

        elif isinstance(obj, Node):
            # 假设 node.children 是 list of 4 elements or None
            for child in obj.children:
                if child:
                    push(child)

    return None  # 没找到任何饭店
