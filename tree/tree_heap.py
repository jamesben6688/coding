class TreeNode:
    def __init__(self, val, level):
        self.val = val
        self.level = level

    def __lt__(self, other):
        if self.level != other.level:
            return self.level > other.level
        else:
            return self.val > other.val


d = {"b": 2, "c": 2, "d": 2, "e": 2}
from heapq import *

nodes = []
for k in d:
    node = TreeNode(k, d[k])
    heappush(nodes, node)

while nodes:
    print(heappop(nodes).val)