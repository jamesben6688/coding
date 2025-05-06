from typing import List
from collections import deque


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed = sorted(changed)

        ans = []
        n = len(changed)
        if n % 2 == 1: return []

        i = n - 1
        que = deque()
        while changed:
            change_pop = changed.pop()
            if change_pop % 2 == 1: return []

            to_be_add = change_pop // 2
            que.append(to_be_add)

            ans.append(to_be_add)

            # if que and not changed or (changed and not que): return []

            while que and que[0] == changed[-1]:
                que.popleft()
                changed.pop()

        return ans if not que else []


print(Solution().findOriginalArray([1,3,4,2,6,8]))