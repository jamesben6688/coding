"""
         1
       /   \
      0     1
     / \   / \
    1   0  1  0

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
    	# 返回包含当前节点node的岛屿的size

        if node is None or node.val == 0 or node in visited:
            return 0  # node是水, 返回0
        visited[node] = True
        size = 1  # Count the current node
        size += dfs(node.left)
        size += dfs(node.right)
        return size

    # Traverse all nodes in the tree
    def traverse(node):
        """
            因为有visited, 所以其实每个节点都只被访问2次, 时间O(N)
        :param node:
        :return:
        """
        if node is None:
            return
        if node.val == 1 and node not in visited:  # 当前节点没有被访问过, 必不可少
            # Start a new island and calculate its size
            island_size = dfs(node)  # 包含当前节点的岛屿的size
            islands.append(island_size)
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return len(islands), islands



root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(0)
root.left.left = TreeNode(1)
root.left.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(1)

print(find_islands(root))
