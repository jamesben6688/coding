from collections import defaultdict


def can_map(src, tgt):
    if len(src) != len(tgt): return False


    m = defaultdict(str)
    reverse_m = defaultdict(str)

    for i in range(len(src)):
        if src[i] in m and m[src[i]] != tgt[i]: return False
        if tgt[i] in reverse_m and reverse_m[tgt[i]] != src[i]: return False

        m[src[i]] = tgt[i]
        reverse_m[tgt[i]] = src[i]

    return True


class UnionFind:
    def __init__(self, n):
        self.father = [x for x in range(n)]

    def find(self, x):
        father_x = self.father[x]
        if father_x != x:
            self.father[x] = self.find(father_x)
        return self.father[x]

    def union(self, x, y):
        father_x = self.find(x)
        father_y = self.find(y)

        if father_x != father_y:
            self.father[father_x] = father_y


def merge_strs(strs):
    n = len(strs)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i+1, n):
            if can_map(strs[i], strs[j]):
                uf.union(i, j)

    groups = defaultdict(list)
    for i in range(n):
        father_i = uf.find(i)
        groups[father_i].append(i)
    ans = []
    for k in groups.keys():
        ans.append(groups[k])

    for i in range(len(ans)):
        ans[i] = [strs[j] for j in ans[i]]
    return ans

print(can_map("aaa", "XYZ"))
print(merge_strs( ["abc", "def", "ghi", "xyz", "foo", "egg", "add"]))
