class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def num_of_island(self, root):
        sizes = []
        def dfs(node):
            if node is None: return 0
            if node.left is None and node.right is None:
                if node.val == 1: return 1
                else: return 0
            l = dfs(node.left)
            r = dfs(node.right)

            ans = l+r
            if node.val == 0:
                return ans
            else:
                if node.left and node.right and node.left.val==1 and node.right.val==1:
                    ans -= 1
                elif node.left and node.right and node.left.val==0 and node.right.val==0:
                    ans += 1
            return ans
        return dfs(root)


root = TreeNode(1,
                left=TreeNode(0,
                              left=TreeNode(1),
                              right=TreeNode(0)),
                right=TreeNode(1,
                               left=TreeNode(1),
                               right=TreeNode(0)))
print(Solution().num_of_island(root))


"""
         1
       /   \
      0     1
     / \   / \
    1   0  1  0

"""