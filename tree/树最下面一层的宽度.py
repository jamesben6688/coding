"""
题目是给一个 binary tree, 问最下边那个level的width。第一个1之前的null不算，最后一个1之后的null也不算。例如
      1
    1    1
     1 1  1
答案就是 3
      1
    1    1
      1   1
答案也是3
这道题很tricky，我用了几次hint才做出来一个完整的答案，听不出来当时小哥的反应。过了2天recruiter通知可以onsite。

bfs？我的想法是：把null也放到队列里最后一行在队列里表现为{null1null1null}然后遍历得到结果补充内容(2022-09-0711:45+08:00):
想了想不用把null也存进去用一个queue<cuple<nodeint>>存节点和对应index则内层宽度可以用队列的first和last相减得到

1先得出tree的height
2通过height得到leaf node leftmost、rightmost的编号（
root node#1  root->left#1*2   root->right#1*2+1  and  so on）

3(#right most-#left most)+1就是最底层levelwidth1
(#1)/\1(#2)1(#3)/
\/1(#4)1(#5)1(#6)------answer6-4+1=3time:O(N)space:O(H)
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def width_of_bottom_level(root):
    if not root:
        return 0

    queue = deque([(root, 0)])  # (node, index)

    last_level_indices = []

    while queue:
        level_size = len(queue)
        level_indices = []

        for _ in range(level_size):
            node, idx = queue.popleft()
            level_indices.append(idx)

            if node.left:
                queue.append((node.left, idx * 2))
            if node.right:
                queue.append((node.right, idx * 2 + 1))

        # Save this level's indices; last one will be bottom level
        print(level_indices)
        if level_indices:
            last_level_indices = level_indices

    return last_level_indices[-1] - last_level_indices[0] + 1


#       1
#     1   1
#    x 1 1 1
# 时空复杂度都是O(N)
root = TreeNode(1,
                TreeNode(1, None,
                         TreeNode(1)),
                TreeNode(1,
                         TreeNode(1),
                         TreeNode(1)))

print(width_of_bottom_level(root))  # Output: 4
