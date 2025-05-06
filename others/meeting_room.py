from heapq import heappop, heappush
from typing import List

class Solution:
    def minMeetingRooms_1(self, intervals: List[List[int]]) -> int:
        """
            扫描线算法: O(nlog(n))
        """

        m = []
        for interval in intervals:
            m.append((interval[0], 1))
            m.append((interval[1], -1))

        m = sorted(m, key=lambda x: (x[0], x[1]))
        cur_rooms = 0
        mx_rooms = 0
        for mm in m:
            cur_rooms += mm[1]
            mx_rooms = max(mx_rooms, cur_rooms)
        return mx_rooms

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
            堆算法
        """
        que = []
        mx_rooms = 0
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        for interval in intervals:
            while que and que[0] <= interval[0]:
                heappop(que)

            heappush(que, interval[1])
            mx_rooms = max(mx_rooms, len(que))
        return mx_rooms
