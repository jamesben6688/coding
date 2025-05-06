"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
# 759

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        times = []
        for ss in schedule:
            for s in ss:
                # print(s)
                times.append((s.start, -1))
                times.append((s.end, 1))

        times = sorted(times)
        # print(times)

        cnt = 0
        ans = []
        for i, t in enumerate(times):
            cnt += t[1]

            if cnt == -1 and t[1] == -1 and i-1 >= 0 and t[0] != times[i-1][0]:
                ans.append(Interval(times[i-1][0], t[0]))
        # print(ans)
        # for inte in ans:
        #     print(inte.start, inte.end)
        return ans