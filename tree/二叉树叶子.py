from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            O(n)一次遍历

        :param root:
        :return:
        """
        ans = []

        def dfs(node):
            if node is None: return -1

            l_depth = dfs(node.left)
            r_depth = dfs(node.right)

            cur = 1 + max(l_depth, r_depth)
            if cur >= len(ans):
                ans.append([])

            ans[cur].append(node.val)

            return cur

        dfs(root)
        return ans

    def findLeaves_1(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        path = []
        def dfs(node, parent, is_left):
            nonlocal path
            if node is None:
                return

            if node.left is None and node.right is None:
                path.append(node.val)
                if is_left:
                    parent.left = None
                else:
                    parent.right = None

            dfs(node.left, node, True)
            dfs(node.right, node, False)

            if node == root:
                ans.append(path[:])
                # path.clear()

        dummy = TreeNode(-1)
        dummy.left = root
        while dummy.left is not None:
            dfs(dummy.left, dummy, True)
            path.clear()

        return ans


"""
        1
    2           3
4       5    
"""

root = TreeNode(1,
                left=TreeNode(2,
                              left=TreeNode(4),
                              right=TreeNode(5)),
                right=TreeNode(3))

print(Solution().findLeaves(root))
