from dataclasses import dataclass
from typing import Optional, List
from collections import defaultdict
import heapq


@dataclass
class Pair:
    c: str
    level: int


class TreeNode:
    def __init__(self, val: str):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class TreeBuilder:
    @staticmethod
    def build_tree(inputs: List[Pair]) -> Optional[TreeNode]:
        # Create a map: level -> min-heap of characters
        chars_by_level = defaultdict(list)
        for p in inputs:
            heapq.heappush(chars_by_level[p.level], p.c)

        # Sorted list of available levels (equivalent to TreeMap in Java)
        levels = sorted(chars_by_level.keys())

        def recursive_helper(cur_level: int) -> Optional[TreeNode]:
            # Stop if there are no keys >= current level
            valid_levels = []
            for l in levels:
                if l >= cur_level and chars_by_level[l]:
                    valid_levels.append(l)
            # valid_levels = [l for l in levels if l >= level and chars_by_level[l]]
            if not valid_levels:
                return None

            if chars_by_level[cur_level]:
                val = heapq.heappop(chars_by_level[cur_level])
                if not chars_by_level[cur_level]:
                    levels.remove(cur_level)
                return TreeNode(val)
            else:
                node = TreeNode('*')
                node.left = recursive_helper(cur_level + 1)
                node.right = recursive_helper(cur_level + 1)
                return node

        root = recursive_helper(0)

        # If chars_by_level not all consumed, return None
        if any(chars_by_level[level] for level in levels):
            return None
        return root


print(TreeBuilder.build_tree([
    Pair(*['e', 1]),
    Pair(*['b', 3]), Pair(*['d', 3])
]))

"""    
            *
    {e, 1},    *
{b, 2}     {z, 2}
                {a, 3}


    {{e, 1}, {b, 2}, {z, 2}

           *
     {e, 1} {b, 1}
{z, 2}

"""