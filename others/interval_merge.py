class Solution:
    def merge(self, intervals):
        """
            插旗: 桶
        """
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        ans = []
        cur = intervals[0]

        i = 1
        n = len(intervals)
        while i < n:
            if intervals[i][0] > cur[1]:
                ans.append(cur)
                cur = intervals[i]
            else:
                cur[0] = min(cur[0], intervals[i][0])
                cur[1] = max(cur[1], intervals[i][1])
            i += 1

        ans.append(cur)
        return ans