"""
       +
      / \
     *   3
    / \
   2   1

"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val  # 运算符或数字（字符串形式）
        self.left = left
        self.right = right
def to_expression(node):
    if not node.left and not node.right:
        return str(node.val)  # 叶子节点直接返回数字

    left_expr = to_expression(node.left)
    right_expr = to_expression(node.right)

    return f"({left_expr} {node.val} {right_expr})"
# 构建表达式树: (2 * 1) + 3
root = TreeNode('+',
    TreeNode('*',
        TreeNode('2'),
        TreeNode('1')
    ),
    TreeNode('3')
)

print(to_expression(root))  # 输出: ((2 * 1) + 3)
