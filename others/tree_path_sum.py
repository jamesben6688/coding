class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def path_sum_leaf2leaf(self, root):
        def dfs(node):
            if node is None: return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            return max(left_sum, right_sum) + node.val
        return dfs(root)

    def path_sum(self, root):
        ans = -float('inf')
        def dfs(node):
            nonlocal ans
            if node is None: return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            ans = max(ans, node.val + max(left_sum, 0) + max(right_sum, 0))

            return node.val + max(max(left_sum, 0), max(right_sum, 0))
        dfs(root)
        return ans
"""
         0
       /   \
      0     1
     / \   / \
    1   0  1  1

"""
root = TreeNode(0,
                left=TreeNode(0,
                              left=TreeNode(1),
                              right=TreeNode(0)),
                right=TreeNode(1,
                               left=TreeNode(1),
                               right=TreeNode(1)))
print(Solution().path_sum_leaf2leaf(root))
print(Solution().path_sum(root))
