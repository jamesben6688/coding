# 同样以 0 为起点
n = 10
adj = [[]]
parent = [0] * n

def dfs(v):
    for u in adj[v]:
        if u != parent[v]:
            parent[u] = v
            dfs(u)

def pruefer_code():
    """
        时间O(N)

    :return:
    """
    n = len(adj)
    parent[n - 1] = -1
    dfs(n - 1)

    ptr = -1
    degree = [0] * n
    for i in range(0, n):
        degree[i] = len(adj[i])
        if degree[i] == 1 and ptr == -1:
            ptr = i

    code = [0] * (n - 2)
    leaf = ptr
    for i in range(0, n - 2):
        next = parent[leaf]
        code[i] = next
        if degree[next] == 1 and next < ptr:
            degree[next] = degree[next] - 1
            leaf = next
        else:
            ptr = ptr + 1
            while degree[ptr] != 1:
                ptr = ptr + 1
            leaf = ptr
    return code

def pruefer_code():
    """
        时间O(Nlg(N))

    :return:
    """
    n = len(adj)
    leafs = set()
    degree = [0] * n
    killed = [False] * n
    for i in range(1, n):
        degree[i] = len(adj[i])
        if degree[i] == 1:
            leafs.intersection(i)
    code = [0] * (n - 2)
    for i in range(1, n - 2):
        leaf = leafs[0]
        leafs.pop()
        killed[leaf] = True
        for u in adj[leaf]:
            if killed[u] == False:
                v = u
        code[i] = v
        if degree[v] == 1:
            degree[v] = degree[v] - 1
            leafs.intersection(v)
    return code