class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def delete_leaves_one_by_one(root):
    path = []
    ans = []
    def is_leaf(node):
        return node and not node.left and not node.right

    def dfs(node, parent, is_left):
        nonlocal  ans, path
        if node is None: return

        if node.left:
            dfs(node.left, node, True)
        elif node.right:
            dfs(node.right, node, False)

        if is_leaf(node):
            path.append(node.val)
            if is_left:
                parent.left = None
            else:
                parent.right = None

    dummy = TreeNode(-1)
    dummy.left = root

    while dummy.left:
        dfs(dummy.left, dummy, True)
        ans.append(path[:])
        path.clear()

    return ans


"""
        1
     /    \
    2      3
   / \       \
  4   5       7
             /
            8
4
5, 2
6
7 3 1
"""

# 构建树
root = TreeNode(1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, None, TreeNode(7, TreeNode(8))))

print(delete_leaves_one_by_one(root))  # Output: [4, 5, 2, 3, 1]
