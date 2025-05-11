"""
给你一个function，call这个function会返回两个节点的 排序如 a -> b，b -> c。
但是这个function不保证每次返回都是unique的，就是可能返复call 5次，返回的都是 a -> b。
给你总共character的个数n，要求输出character之间的顺序。
我说了解法是先keep call这个function直到见到n个character，或者直到见过 n *(n-1)/2 个relationship。
他说如果告诉了你 a->b, b->c,你不需要 a->c了，我说我不会。
他说保持拓扑排序的时候，在输出所有character之前，queue里面的size只为1，不为1就一直call function。
"""
from collections import defaultdict, deque

def find_unique_topo_order(n, get_order, max_attempts=100000):
    graph = defaultdict(set)
    indegree = defaultdict(int)
    seen_pairs = set()
    all_chars = set()

    def build_queue():
        return deque([ch for ch in all_chars if indegree[ch] == 0])

    steps = 0
    while steps < max_attempts:
        a, b = get_order()
        all_chars.update([a, b])

        if (a, b) not in seen_pairs:
            seen_pairs.add((a, b))
            if b not in graph[a]:
                graph[a].add(b)
                indegree[b] += 1

        # Only try topological sort when we know all n characters
        # 关系未确定, 继续call
        if len(all_chars) < n:
            steps += 1
            continue

        # Try a dry-run of topological sort to check queue size uniqueness
        temp_indegree = indegree.copy()
        queue = build_queue()
        result = []

        unique = True
        while queue:
            # 关系不唯一, 继续call
            if len(queue) != 1:
                unique = False
                break

            node = queue.popleft()
            result.append(node)

            for nei in graph[node]:
                temp_indegree[nei] -= 1
                if temp_indegree[nei] == 0:
                    queue.append(nei)

        if unique and len(result) == n:
            return result

        steps += 1

    raise ValueError("Failed to determine unique order within limit")
