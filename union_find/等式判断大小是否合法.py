from collections import defaultdict

from collections import defaultdict, deque

def is_valid_relations(relations):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    nodes = set()

    digits = set()
    def parse(expr):
        if '>' in expr:
            u, v = expr.split('>')
            u, v = u.strip(), v.strip()
            if u.isdigit():
                digits.add(u)
            if v.isdigit():
                digits.add(v)
            return u, v  # u > v => u → v
        elif '<' in expr:
            u, v = expr.split('<')
            u, v = u.strip(), v.strip()
            if u.isdigit():
                digits.add(u)
            if v.isdigit():
                digits.add(v)
            return v, u  # a < b => b → a

    # 建图并统计入度
    for rel in relations:
        u, v = parse(rel)
        graph[u].append(v)
        indegree[v] += 1
        nodes.add(u)
        nodes.add(v)
    digits = sorted(list(digits), key=lambda x: int(x))
    for i in range(len(digits)-1):
        graph[digits[i+1]].append(digits[i])
        indegree[digits[i]] += 1


    # 拓扑排序
    queue = deque([node for node in nodes if indegree[node] == 0])
    count = 0

    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # 如果不能遍历所有节点，说明有环
    return count == len(nodes)


# relations1 = ["a > b", "b > 2", "a < 2"]  # 逻辑上：a < 2, a > b > 2 → a > 2 ❌
# print(is_valid_relations(relations1))  # False

relations2 = ["a > b", "b > 2", "a < 3"]
print(is_valid_relations(relations2))  # True
