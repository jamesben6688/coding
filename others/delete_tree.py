class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def delete_tree(root):
    if root is None:
        return

    # Recursively delete the left and right subtrees
    delete_tree(root.left)
    delete_tree(root.right)

    # "Delete" the current node (by setting it to None)
    root.left = None
    root.right = None
    v = root.val
    root.val = None  # Setting value to None, simulating deletion

    print(f"Node with value {v} deleted.")  # Simulating the deletion action

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Delete the tree
delete_tree(root)
