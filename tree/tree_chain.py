"""
一个tree里，一个节点如果不是leaf node也不是有两个child的节点就算chain node，
从上到下这样的节点串起来不中断就是一个chain，数最长的chain，
第二题就是模拟装货，求装完后的顺序，基本就是实现一个stack到queue，考你对数据结构的熟悉
"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longest_chain(self, root):
        ans = None
        mx_len = 0
        def dfs(node):
            nonlocal mx_len, ans
            if node is None or node.left is None and node.right is None:
                return 0

            left_len = dfs(node.left)
            right_len = dfs(node.right)

            if node.left is None and node.right is not None:
                if right_len + 1 > mx_len:
                    ans = node
                    mx_len = right_len + 1
                return right_len + 1

            if node.right is None and node.left is not None:
                if left_len + 1 > mx_len:
                    ans = node
                    mx_len = left_len + 1
                return left_len + 1

            return 0

        dfs(root)
        return ans, mx_len


"""
      A
     /
    B
   /
  C
 / \
D   E

"""
# 构建树结构
A = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")

A.left = B
B.left = C
C.left = D
C.right = E
# D.right = E

# 执行测试
sol = Solution()
print("Longest chain length:", sol.longest_chain(A))  # 应该输出 4

print(Solution().longest_chain(A))