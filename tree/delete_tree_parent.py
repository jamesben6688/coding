"""

树所有的节点都没有child指针，只有parent指针，然后给你一个deleted node，
让你在这个树上找deleted node，然后delete subtree，要求空间必须是O1的

直接delete_node.parent=None
"""


"""
    以下是O(lgN)空间
"""
def delete_node(parents, target):
    # 删除目标节点及其子树
    def dfs(node):
        for i in range(len(parents)):
            # 如果这个节点的父节点是当前节点，那么它就是当前节点的子节点
            if parents[i] == node:
                dfs(i)
        parents[node] = -2  # 标记节点已删除（通过标记为 -2，代表删除）

    dfs(target)  # 从目标节点开始递归删除
