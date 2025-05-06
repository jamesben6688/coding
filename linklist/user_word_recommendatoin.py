"""
用户在点开搜索框后，提供最近的K个搜索输入作为关键词推荐。然后这次的输入也将用于下次的推荐。例子：
search history:
paris
tokyo
seattle
K= 2， 那么应该给出的就是：
paris
tokyo
注意：需要按时间排序，最近的搜索历史应该排在前面。如果历史里有重复的，就只记最近的一次。
follow-up: 如何k是一百万怎么办。: 分布式, 负载均衡
题目不难，很快做出来了。但是开始的时候没认真读题，以为是用trie做top k 推荐呢，被面试官纠正了。

"""

from collections import defaultdict


class Node:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt


class Solution:
    def __init__(self):
        self.head = Node(None)
        self.key_map = defaultdict(Node)

    def add(self, word):
        node = Node(word)
        after_head = self.head.nxt

        node.nxt = after_head
        if after_head:
            after_head.prev = node

        self.head.nxt = node
        node.prev = self.head

        self.key_map[word] = node

    def remove(self, word):
        node = self.key_map[word]

        prev_node = node.prev
        after_node = node.nxt

        if prev_node:
            prev_node.nxt = after_node
        if after_node:
            after_node.prev = prev_node
        self.key_map.pop(word)

    def get_topk(self, k):
        ans = []
        cur = self.head.nxt
        i = 0
        while i < k and cur:
            ans.append(cur.val)
            i += 1
            cur = cur.nxt
        return ans

    def search(self, word):
        if word in self.key_map:
            self.remove(word)

        self.add(word)


s = Solution()
s.add("pairs")
s.add("tokyo")
s.add("nyc")
s.search("tokyo")

print(s.get_topk(3))
