# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def num_of_islands(self, root):
#         ans = 0
#         def dfs(root):
#             """
#                 返回当前节点是岛屿还是水。
#                 1. 当前节点是岛屿, 直接返回1, 不对节点作任何处理
#                 2. 当前节点是水, 需要检查left和right, 如果是岛屿, ans+1; 如果是水不动
#
#                 也就是说只有: 当前节点是水, left是陆地, ans+1, 或者right时陆地, ans+1
#             :param root:
#             :return:
#             """
#             nonlocal ans
#             if root is None:
#                 return 0
#
#             left = dfs(root.left)
#             right = dfs(root.right)
#
#             if root.val == 1: return 1
#             else:
#                 if left: ans += 1
#                 if right: ans += 1
#                 return 0
#
#         t = dfs(root)
#         if t:
#             ans += 1
#         return ans

"""
         1
       /   \
      0     0
     / \   / \
    1   0  1  1

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_islands(root):
    if root is None:
        return 0, []

    islands = []
    visited = {}

    # Helper function to perform DFS and calculate the size of an island.
    def dfs(node):
        if node is None or node.val == 0 or node in visited:
            return 0
        visited[node] = True
        size = 1  # Count the current node
        size += dfs(node.left)
        size += dfs(node.right)
        return size

    # Traverse all nodes in the tree
    def traverse(node):
        if node is None:
            return
        if node.val == 1 and node not in visited:
            # Start a new island and calculate its size
            island_size = dfs(node)
            islands.append(island_size)
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return len(islands), islands



root = TreeNode(0)
root.left = TreeNode(0)
root.right = TreeNode(0)
root.left.left = TreeNode(1)
root.left.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(1)

print(find_islands(root))
# print(Solution().num_of_islands(root))