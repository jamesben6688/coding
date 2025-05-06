"""
判断两个图是否一样，取决于你想判断“图结构是否相同”还是“图的表示是否完全相等”。下面我会给你几种情况的处理方式：

✅ 你可能的输入形式
比如图是邻接表：

python
Copy
Edit
graph1 = {
    1: [2, 3],
    2: [1],
    3: [1]
}

graph2 = {
    3: [1],
    1: [3, 2],
    2: [1]
}
这里两个图其实是一样的，尽管键的顺序不一样，value 的列表顺序也不一样。

✅ 解法：结构是否一样（无向图）
python
Copy
Edit
def graphs_are_equal(g1, g2):
    if set(g1.keys()) != set(g2.keys()):
        return False

    for node in g1:
        if set(g1[node]) != set(g2[node]):
            return False

    return True
✅ 示例
python
Copy
Edit
g1 = {
    1: [2, 3],
    2: [1],
    3: [1]
}

g2 = {
    3: [1],
    1: [3, 2],
    2: [1]
}

print(graphs_are_equal(g1, g2))  # True
🧠 补充讨论
✅ 如果图是有向图？
你仍然可以使用上面的代码，只要 g1[node] 是所有 出边的目标节点列表。

✅ 如果图是邻接矩阵？
那就直接比较两个二维矩阵是否一样：

python
Copy
Edit
def equal_adj_matrix(g1, g2):
    return g1 == g2
✅ 如果要判断同构图（结构一样，但节点编号不同）？
那是图同构问题，比上面复杂很多，要用到 BFS/DFS 甚至库（例如 networkx）。
"""


