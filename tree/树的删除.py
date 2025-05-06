"""
第一问是从左到右删叶子节点，但是如果删完一个节点后，它的父节点也变成了叶子节点，有限删除这个父节点；第二问就是利口 要灵儿，
每轮删除都是从左到右删除所有的叶子节点；第三问是，可以删除任意叶子节点，求输出所有可能的删除顺序

第一问：从左到右删叶子节点，但一旦删除叶子后其父也变成叶子，就接着删这个父
这是一个“一口气往上删到底”的做法，但每次删除从左到右。

示例：
markdown
Copy
Edit
       1
      / \
     2   3
    /
   4
第一步删叶子：4、3（从左到右）

然后 2 变成叶子，也删掉

然后 1 变成叶子，也删掉

删除顺序：[4, 3, 2, 1]
实现思路：
每次从左到右找叶子，删掉它

如果某节点的左右子树都删了，它变成新的叶子，继续删

✅ 第二问：Leetcode 366 — 每轮删除所有叶子节点，按轮次输出
这里是一轮一轮地删叶子，而不是像第一问那样一口气删到顶。

示例同上：
markdown
Copy
Edit
       1
      / \
     2   3
    /
   4
第1轮删：4、3 → [[4, 3]]

第2轮删：2 → [[4, 3], [2]]

第3轮删：1 → [[4, 3], [2], [1]]

思路：
用 DFS 后序遍历，节点的“高度”决定它在哪一轮被删除（叶子是第 0 层）

LC366 原题参考代码（高度分组）：
python
Copy
Edit
def findLeaves(root):
    res = []
    def dfs(node):
        if not node: return -1
        level = 1 + max(dfs(node.left), dfs(node.right))
        if level == len(res):
            res.append([])
        res[level].append(node.val)
        return level
    dfs(root)
    return res
✅ 第三问：可以删除任意叶子节点，求所有可能的删除顺序
这是一个 回溯 / DFS 的全排列变种问题。

示例：
Copy
Edit
   1
  / \
 2   3
初始叶子：2, 3。你可以选择先删 2 再删 3，也可以先删 3 再删 2。

删除顺序可能是：
[2, 3, 1]

[3, 2, 1]

思路：
每一轮找所有当前的叶子

对这些叶子做全排列（可以任选一个删）

继续递归下去

伪代码思路：
python
Copy
Edit
def backtrack(tree, path):
    if tree is empty:
        results.append(path)
        return
    leaves = find_all_leaves(tree)
    for leaf in leaves:
        remove(leaf)
        backtrack(tree, path + [leaf.val])
        restore(leaf)



"""