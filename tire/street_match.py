from collections import defaultdict


"""
题目是给你一个地址簿存着一系列地址，大致是 (街道号码，街道名称，城市名称，所在州) 这样的格式， 
e.g.,[(“1”, “Main”, “San Jose”, “CA”), ("1", "Main", "Austin", "TX")]。
要考虑不同的城市可能存在一样的街道， 不同的州存在同样的城市等等等等的情况
问题是有一系列query（很多很多), 判断有没有match.
query的格式可能存在以下几种情况。 有些elem可能存在NULL，这个时候如果其它的匹配上也认为是找到了match
query = (“1”, “Main”, “San Jose”, “CA”) --> found match
query = (“1”, “Main”, “San Jose”, None) --> found match
query = (“1”, “Main”, None, None) --> found match
query = (“22”, “Main”, “San Jose”, “CA”) --> no match
"""
class TireNode:
    def __init__(self, val):
        self.val = val
        self.children = defaultdict(TireNode)


class Solution:
    def __init__(self):
        self.root = TireNode(None)

    def build(self, address):
        cur = self.root
        for a in address:
            for i in range(3, -1, -1):
                if a[i] not in cur.children:
                    cur.children[a[i]] = TireNode(a[i])
                cur = cur.children[a[i]]

    def query(self, query):
        def dfs(node, idx):
            if idx == -1:
                return True

            if query[idx] in node.children:
                if dfs(node.children[query[idx]], idx-1):
                    return True
            elif query[idx] is None:
                for child in node.children:
                    if dfs(node.children[child], idx-1):
                        return True

            return False

        return dfs(self.root, 3)


s = Solution()
s.build([("1", "Main", "San Jose", "CA"), ("1", "Main", "Austin", "TX")])

print(s.query(("1", "Main", "San Jose", "CA")))
print(s.query(("1", "Main", "San Jose", None)))
print(s.query(("1", "Main", None, None)))
print(s.query(("22", "Main", "San Jose", "CA")))
