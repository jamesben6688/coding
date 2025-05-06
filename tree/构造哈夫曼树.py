from collections import defaultdict
from sortedcontainers.sorteddict import SortedDict
from heapq import *


"""
哈弗曼树构造过程
https://www.cnblogs.com/minqiliang/p/16828759.html
"""
class TreeNode:
    def __init__(self, val, level, id, left=None, right=None):
        self.id = id
        self.val = val
        self.level = level
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.level != other.level:
            return self.level > other.level
        elif self.val == '*' and other.val != "*":
            return True
        elif self.val != "*" and other.val == '*':
            return False
        elif self.val != other.val:
            return ord(self.val) > ord(other.val)
        else:
            return self.id < other.id



class Solution:
    def build_haffman(self, levels):
        cnt = 0
        nodes = []
        heapify(nodes)

        for val, level in levels.items():
            # nodes.append(TreeNode(val, level, cnt))
            heappush(nodes, TreeNode(val, level, cnt))
            cnt += 1

        # nodes = sorted(nodes)
        # while nodes:
        #     print(heappop(nodes).val)

        while len(nodes) > 1:
            level_cnt = nodes[0].level

            cur_cnt = 0
            while nodes[0].level == level_cnt:
                cur_cnt += 2

                if cur_cnt > 2 ** level_cnt:
                    return None

                new_node = TreeNode("*", level_cnt-1, id=cnt)
                cnt += 1
                new_node.right = heappop(nodes)

                if nodes[0].level != level_cnt:
                    return None

                new_node.left = heappop(nodes)
                heappush(nodes, new_node)


        root = nodes[0]
        return root


print(Solution().build_haffman({"c": 2, "d": 2, "f": 1}))
