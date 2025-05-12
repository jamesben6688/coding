from sortedcontainers import SortedList

class PointManager:
    def __init__(self):
        self.points = set()
        self.xs = SortedList()
        self.ys = SortedList()

    def add(self, x, y):
        if (x, y) not in self.points:
            self.points.add((x, y))
            self.xs.add(x)
            self.ys.add(y)

    def remove(self, x, y):
        if (x, y) in self.points:
            self.points.remove((x, y))
            self.xs.remove(x)
            self.ys.remove(y)

    def get_bbox(self):
        if not self.points:
            return None
        return (self.xs[0], self.ys[0], self.xs[-1], self.ys[-1])
