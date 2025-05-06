"""
1. insert。就是插入一个integer
2. get。假设之前插入的所有数的中位数是x，那么这个get操作需要返回任意的一个数y，y必须满足x <= y <= x*2
"""

from sortedcontainers import SortedList

class MedianRangeDataStructure:
    def __init__(self):
        self.sorted_list = SortedList()

    def insert(self, num: int):
        self.sorted_list.add(num)

    def get(self) -> int:
        n = len(self.sorted_list)
        x = self.sorted_list[n // 2]  # upper median
        i = self.sorted_list.bisect_left(x)
        while i < n:
            y = self.sorted_list[i]
            if y <= 2 * x:
                return y
            i += 1
        return -1
