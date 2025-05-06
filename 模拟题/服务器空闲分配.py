from typing import *
from heapq import *


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        busy = []
        n = len(servers)
        idel = [(servers[i], i) for i in range(n)]
        heapify(idel)

        ans = []
        for i in range(len(tasks)):
            while busy and busy[0][0] <= i:
                pass
            if len(idel):
                cur_w, cur_i = heappop(idel)
                ans.append(cur_i)
                heappush(busy, (i+tasks[i], i))
            else:
                cur_t, cut_i = heappop(busy)
                ans.append(cur_i)
                heappush(busy, (max(cur_t, i)+tasks[i], i))
        return ans


print(Solution().assignTasks(
servers =
[3,3,2],
tasks =
[1,2,3,2,1,2]
))

