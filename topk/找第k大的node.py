"""
Given list of N nodes, node object has (id, value, label). return K largest node by value, which satisfy
that no more than M nodes having the same label.
✅ 方法总结：
我们要从 N 个 node 中，选出最大 K 个 node，要求：

每种 label 最多只能出现 M 次。

✅ 解法步骤：
按 label 分组：把节点按 label 分到不同 list（总共 L 个 label）。

每个 label 内部：对每个 label 的节点，用 QuickSelect 拿到它们中 top M 大的节点（最多 M 个）。

合并所有保留的节点：这些节点数量 ≤ L × M。

再对合并后的节点应用 QuickSelect，找到 top K。

✅ 时间复杂度（期望）：
第一步（分组）：O(N)

第二步（每组 QuickSelect）：O(M) 平均，但总是 ≤ N，总复杂度 O(N)

第三步（合并）：O(N)

第四步（最终 QuickSelect）：O(K) ≤ O(N)

总期望时间复杂度：O(N)
"""

import random
from collections import defaultdict

class Node:
    def __init__(self, id, value, label):
        self.id = id
        self.value = value
        self.label = label
    def __repr__(self):
        return f"Node(id={self.id}, value={self.value}, label={self.label})"

def quick_select(nodes, k):
    if len(nodes) <= k:
        return nodes
    pivot = random.choice(nodes).value
    left = [n for n in nodes if n.value > pivot]
    mid = [n for n in nodes if n.value == pivot]
    right = [n for n in nodes if n.value < pivot]

    if len(left) >= k:
        return quick_select(left, k)
    elif len(left) + len(mid) >= k:
        return left + mid[:k - len(left)]
    else:
        return left + mid + quick_select(right, k - len(left) - len(mid))

def top_k_largest_nodes(nodes, K, M):
    label_groups = defaultdict(list)
    for node in nodes:
        label_groups[node.label].append(node)

    candidates = []
    for group in label_groups.values():
        top_m = quick_select(group, M)
        candidates.extend(top_m)

    return quick_select(candidates, K)


nodes = [
    Node(1, 100, "a"),
    Node(2, 90, "a"),
    Node(3, 85, "b"),
    Node(4, 95, "c"),
    Node(5, 80, "a"),
    Node(6, 70, "b"),
    Node(7, 60, "d"),
    Node(8, 98, "c"),
    Node(9, 65, "d")
]
res = top_k_largest_nodes(nodes, K=4, M=2)
print(res)
