"""

 ["a", "at", "sin", "si", "s", "eat"]
 ->eat
"""
from typing import List
from collections import defaultdict, Counter
from copy import deepcopy


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda x: len(x))

        """
            dp[i] = dp[j] + 1
        """
        cnt = Counter()
        chain = defaultdict(list)
        mx = [0, []]
        ans = set()
        for w in words:
            for i in range(len(w)):
                prev = w[:i]+w[i+1:]
                if 1+cnt[prev] > cnt[w]:
                    cnt[w] = 1 + cnt[prev]
                    chain[w] = chain[prev] + [w]
                # cnt[w] = max(cnt[w], cnt[prev]+1)
                # mx = max(mx[0], cnt[w])
                if cnt[w] > mx[0]:
                    mx = [cnt[w], chain[w]]
                #     ans = set()
                #     ans.add(chain[w])
                # elif cnt[w] == mx[0]:
                #     ans.add(deepcopy(chain[w]))
        print(mx[1], ans)
        return mx[0]



print(Solution().longestStrChain(
    ["a", "at", "sin", "si", "s", "eat", "beat"]
))