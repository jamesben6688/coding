class Node:
    def __init__(self, val, size, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.size = size


tree = Node(44, 9,
            Node(20, 3,
                 Node(12, 1),
                 Node(31, 1)),
            Node(61, 5,
                 Node(55, 1),
                 Node(70, 3,
                      Node(65, 1),
                      Node(71, 1))),
)


def get_node(root, n) -> [Node, None]:
    ans = None
    def get_ith_node(root, n):
        nonlocal ans
        if root.left is None and root.right is None:
            ans = root
            return

        if n == root.left.size + 1:
            ans = root
            return
        elif n > root.left.size + 1:
            get_ith_node(root.right, n-root.left.size-1)
        else:
            get_ith_node(root.left, n)
    get_ith_node(root, n)
    return ans

for i in range(1, 7):
    print(get_node(tree,i).val)
