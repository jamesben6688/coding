class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def num_of_island(self, root):
        sizes = []
        visited = set()
        def dfs(node):
            if node is None or node.val == 0:
                return 0
            visited.add(node)
            size = 1
            l_size = dfs(node.left)
            r_size = dfs(node.right)
            return size+l_size+r_size

        def traverse(node):
            if node is None: return
            if node.val == 1 and node not in visited:
                size = dfs(node)
                sizes.append(size)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return sizes  # dfs(root)


root = TreeNode(1,
                left=TreeNode(0,
                              left=TreeNode(1),
                              right=TreeNode(0)),
                right=TreeNode(0,
                               left=TreeNode(1),
                               right=TreeNode(0)))
print(Solution().num_of_island(root))


"""
         1
       /   \
      0     0
     / \   / \
    1   0  1  0

"""