# Tree:
#      6
#     / \
#   4    2
#  /
# 1



def dfs(node):
    if not node.left and not node.right:
        return node.cost, 0

    left_cut, left_not_cut = 0, 0
    if node.left:
        left_cut, left_not_cut = dfs(node.left)
    right_cut, right_not_cut = 0, 0
    if node.right:
        right_cut, right_not_cut = dfs(node.right)

    parent_cost = node.cost
    one = parent_cost + min(left_cut + right_not_cut, right_cut + left_not_cut)
    two = left_cut + right_cut
    return one, two


class TreeNode:
    def __init__(self, val, cost):
        self.val = val
        self.left = None
        self.right = None
        self.cost = cost

"""
          (6, 0)
    (4, 5)      (2, 1)
(1, 10)  (3, 2)
"""

# Creating the tree
root = TreeNode(6, 0)
root.left = TreeNode(4, 5)
root.right = TreeNode(2, 1)
root.left.left = TreeNode(1, 10)
# root.left.right = TreeNode(3, 2)

print(dfs(root))
