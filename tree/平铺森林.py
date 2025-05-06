class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten_trees(trees):

    stack = []
    res = set()
    for tree in trees:
        cur = tree

        while stack or cur:
            while cur:
                stack.append(cur)
                if cur != tree:
                    res.add(cur)
                cur = cur.left

            cur = stack.pop().right

    roots = []
    for tree in trees:
        if tree not in res:
            roots.append(tree)

    ans = []

    def dfs(node):
        if node is None: return

        dfs(node.left)
        dfs(node.right)
        ans.append(node.val)

    for r in roots:
        dfs(r)

    return ans


# 构造小树们
a = Node('A')
b = Node('B')
c = Node('C')

a.left = b
b.left = c

trees = [a, b]  # A和B都是最开始的小树

print(flatten_trees(trees))  # 输出 ['C', 'B', 'A']

