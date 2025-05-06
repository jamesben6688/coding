from typing import List
from heapq import *


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        n = len(paint)
        pts = []
        ans = [0 for _ in range(n)]
        for idx, p in enumerate(paint):
            pts.append((p[0], 1, idx))
            pts.append((p[1], -1, idx))

        # print(pts)
        pts = sorted(pts, key=lambda x: (x[0], x[1], x[2]))

        prev = None
        cur_paints = []
        to_be_removed = set()
        for i in range(len(pts)):
            if pts[i][1] == 1:
                heappush(cur_paints, pts[i][2])
            else:
                to_be_removed.add(pts[i][2])

            while to_be_removed and cur_paints[0] in to_be_removed:
                to_be_removed.remove(cur_paints[0])
                heappop(cur_paints)

            if cur_paints:
                ans[cur_paints[0]] += pts[i + 1][0] - pts[i][0]

            # if pts[i][0] > pts[i-1][0]:
            #     ans[cur_paints[0]] += pts[i][0] - pts[i-1][0]
        return ans


print(Solution().amountPainted(
    paint = [[0,5],[0,2],[0,3],[0,4],[0,5]]
))