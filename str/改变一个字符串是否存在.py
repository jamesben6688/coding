"""
1554
"""
from typing import List
from collections import defaultdict


class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        seen = set()
        for d in dict:
            for i in range(len(d)):
                cur = d[:i] + "*" + d[i + 1:]
                h = hash(cur)
                if h in seen:
                    return True
                seen.add(h)
        return False


print(Solution().differByOne(
["abcde","abaaa","aaade"]
))