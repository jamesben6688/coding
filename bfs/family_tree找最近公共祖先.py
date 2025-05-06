"""
family tree的最近公共最先

这题确实比普通的最近公共祖先（Lowest Common Ancestor, LCA）问题难不少，因为：

每个人可以有两个父母 → 树变成了 有向无环图（DAG）

所以祖先是从一个点向上扩展，不是树，而是 DAG 的子图

如果 naive 地 DFS 每个祖先，会有 指数级别的重复遍历

优化点在于 避免重复遍历 和 同时向上合并路径

🧠 思路：双向 BFS + HashSet 记录祖先路径
我们的问题是：

给定一个 family tree（每人最多两个 parent），找两个人最近的共同祖先。

✅ 算法步骤：
建图：记录每个人的父母 parents[node] = [p1, p2]

双向 BFS（从 node1 和 node2 同时向上找祖先）

用两个 set 记录每个人到的祖先路径 visited1 和 visited2

如果有交集（visited1 & visited2），第一个交集就是最近祖先

为了保证“最近”，用 BFS（层级往上），遇到交点就返回



"""


from collections import deque, defaultdict

def find_common_ancestor(parents_map, person1, person2):
    def bfs(start):
        visited = set()
        queue = deque([start])
        while queue:
            curr = queue.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            for p in parents_map.get(curr, []):
                queue.append(p)
        return visited

    # 优化版：双向 BFS
    visited1 = set([person1])
    visited2 = set([person2])
    q1 = deque([person1])
    q2 = deque([person2])

    while q1 or q2:
        for _ in range(len(q1)):
            node = q1.popleft()
            for p in parents_map.get(node, []):
                if p in visited2:
                    return p
                if p not in visited1:
                    visited1.add(p)
                    q1.append(p)

        for _ in range(len(q2)):
            node = q2.popleft()
            for p in parents_map.get(node, []):
                if p in visited1:
                    return p
                if p not in visited2:
                    visited2.add(p)
                    q2.append(p)

    return None  # no common ancestor



parents_map = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'G': ['C'],
    'H': ['G'],
}

# A 和 H 的最近祖先是 C
print(find_common_ancestor(parents_map, 'A', 'H'))  # 输出: C

"""
    找路径的话, 就是先找到LCA, 然后从LCA DFS回溯。
"""