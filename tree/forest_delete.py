from collections import defaultdict, deque


def delete_node_and_rebuild(parent, delete_index):
    n = len(parent)

    # 1. 建图
    tree = defaultdict(list)
    for i in range(n):
        if parent[i] != -1:
            tree[parent[i]].append(i)

    # 2. 找到所有需要删除的节点
    to_delete = set()
    queue = deque([delete_index])
    while queue:
        node = queue.popleft()
        to_delete.add(node)
        for child in tree.get(node, []):
            queue.append(child)

    # 3. 保留未删除的节点
    remaining_nodes = [i for i in range(n) if i not in to_delete]

    # 4. 建立旧索引 -> 新索引映射
    old_to_new = {old: new for new, old in enumerate(remaining_nodes)}

    # 5. 构建新parent数组
    new_parent = []
    for old_index in remaining_nodes:
        p = parent[old_index]
        if p == -1 or p in to_delete:
            new_parent.append(-1)
        else:
            new_parent.append(old_to_new[p])

    return new_parent
