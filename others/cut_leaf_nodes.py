class TreeNode:
    def __init__(self, val, edge_cost, left=None, right=None):
        self.val = val
        self.edge_cost = edge_cost
        self.left = left
        self.right = right


class Solution:
    def min_cost(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.edge_cost

        left = 0
        right = 0
        if root.left is not None:
            left = self.min_cost(root.left)

        if root.right is not None:
            right = self.min_cost(root.right)

        # special case for handling root node
        if root.edge_cost == 0:
            # 该节点为root
            return left + right
        else:
            # 非root, 两种情况
            return min(left + right, root.edge_cost)


root = TreeNode(6, 0)
root.left = TreeNode(4, 5)
root.right = TreeNode(2, 1)
root.left.left = TreeNode(1, 10)

print(Solution().min_cost(root))
