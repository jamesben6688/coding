class TreeNode:
    def __init__(self, val, size, left=None, right=None):
        self.val = val
        self.size = size
        self.left = left
        self.right = right


class Solution:
    """
        O(Lg(N))

    """
    def get_ele(self, root, i):
        def dfs(node, idx):
            if node.left is None and node.right is None:
                return node.val

            if node.left.size==idx-1:
                return node.val
            elif node.left.size > idx-1:
                return dfs(node.left, idx)
            else:
                return dfs(node.right, idx-node.left.size-1)

        return dfs(root, i)


tree = TreeNode(44, 9,
                TreeNode(20, 3,
                         TreeNode(12, 1),
                         TreeNode(31, 1)),
                TreeNode(61, 5,
                         TreeNode(55, 1),
                         TreeNode(70, 3,
                                  TreeNode(65, 1),
                                  TreeNode(71, 1)))
                )
s = Solution()
for i in range(9):
    print(i+1, s.get_ele(tree, i+1))
