class Solution:
    def non_overlap_intervals(self, intervals):
        ans = []

        pins = []
        cnt = 0
        for interval in intervals:
            pins.append((interval[0], -1))
            pins.append((interval[1], 1))

        pins = sorted(pins, key=lambda x: (x[0], x[1]))

        for i, p in enumerate(pins):
            cnt += p[1]
            if cnt == -2 or cnt == 0:
                if i-1 >= 0 and pins[i][0] != pins[i-1][0]:
                    ans.append([pins[i-1][0], pins[i][0]])
        return ans


print(Solution().non_overlap_intervals(
    [
        [1, 3], [2, 5]
    ]
))

