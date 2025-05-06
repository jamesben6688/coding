from typing import List
from heapq import *
from collections import defaultdict


class Solution:
    def rectangleArea(self, rs: List[List[int]]) -> List:
        def resolve_intervals(intervals):
            """
            区间处理
            https://www.bilibili.com/video/BV1h3411P7Nd/?spm_id_from=333.337.search-card.all.click&vd_source=515dedd17a7416a93307429c1b2dfa6b
            :param intervals:
            :return:
            """
            # 所有事件: (position, type, priority, id)
            events = []
            for l, r, id_, p in intervals:
                events.append((l, 0, -p, id_))  # 负优先级为了 max-heap 效果
                events.append((r, 1, -p, id_))

            # 排序：位置 → enter 优先 → priority 越大越先
            events.sort()

            # 当前活跃区间（用 max heap 模拟）
            active = []
            removed = set()
            result = defaultdict(list)

            n = len(events)
            to_be_removed = set()
            for i in range(n):
                if events[i][1] == 0:
                    heappush(active, (events[i][2], events[i][3]))
                else:
                    to_be_removed.add(events[i][3])

                while to_be_removed and active[0][1] in to_be_removed:
                    to_be_removed.remove(active[0][1])
                    heappop(active)

                if active and events[i+1][0] > events[i][0]:
                    result[active[0][1]].append([events[i][0], events[i+1][0]])
            return result

        ans = [0 for _ in range(len(rs))]
        ps = []
        for info in rs:
            ps.append(info[0])
            ps.append(info[2])
        ps.sort()
        for i in range(1, len(ps)):
            a, b = ps[i - 1], ps[i]
            width = b - a
            if width == 0:
                continue
            ranges = []
            for info in rs:
                if info[0] <= a and info[2] >= b:
                    ranges.append((info[1], info[3], info[4], info[5]))
            ranges = resolve_intervals(ranges)  # Nlg(N)

            # print(ranges)
            for r in ranges:  # O(N)
                for left, right in ranges[r]:
                    ans[r] += width * (right-left)

        return ans


print(Solution().rectangleArea(
    rs = [[0,0,2,2, 0, 3],[1,0,2,3, 1, 2],[1,0,3,1, 2, 1]]
))