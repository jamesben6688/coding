from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder(self, root):
        ans = []
        cur = root
        stack = []
        while cur or len(stack) > 0:
            while cur:
                stack.append(cur)
                ans.append(cur.val)
                cur = cur.left

            cur = stack.pop().right
        return ans

    def inorder(self, root):
        ans = []
        cur = root
        stack = []
        while cur or len(stack) > 0:
            while cur:
                stack.append(cur)
                cur = cur.left

            node = stack.pop()
            ans.append(node.val)
            cur = node.right
        return ans

    def postorder(self, root):
        ans = deque()
        cur = root
        stack = []
        while cur or len(stack) > 0:
            while cur:
                stack.append(cur)
                ans.appendleft(cur.val)
                cur = cur.right

            cur = stack.pop().left

        return ans


"""
   1
 2   5            
3 4 6 7            

"""
root = TreeNode(1,
                left=TreeNode(2,
                              left=TreeNode(3),
                              right=TreeNode(4)),
                right=TreeNode(5,
                               left=TreeNode(6),
                               right=TreeNode(7)))
print(Solution().preorder(root))
print(Solution().inorder(root))
print(Solution().postorder(root))
