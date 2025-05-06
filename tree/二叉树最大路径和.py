class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_maxsum(self, root):
        mx_sum = -float('inf')
        path_sum = 0
        path = []
        def dfs(node):
            nonlocal mx_sum, path_sum

            if node is None: return
            path.append(node.val)
            path_sum += node.val

            if node is None or node.left is None and node.right is None:
                mx_sum = max(mx_sum, path_sum)
                print(path)
            # path.append(node.val)
            # path_sum += node.val
            dfs(node.left)
            # path_sum -= node.val
            dfs(node.right)
            path.pop()
            path_sum -= node.val

        dfs(root)
        return mx_sum


root = TreeNode(4,
                left=TreeNode(9,
                              left=TreeNode(5),
                              right=TreeNode(1)),
                right=TreeNode(0))

print(Solution().get_maxsum(root))

