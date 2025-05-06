def merge_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
    ans = []
    cur = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= cur[1]:
            cur[1] = intervals[i][1]
        else:
            ans.append(cur)
            cur = intervals[i]

    ans.append(cur)
    return ans


def range_summary(intervals, mn, mx):
    ans = []


def available_days(person_times, max_days, num_people):
    intervals = []
    for p_idx, s, e in person_times:
        intervals.append([s, e])
    intervals = merge_intervals(intervals)

    return range_summary(intervals)



person_times = [
    [1, 1, 1],
    [2, 20, 20],
    [3, 5, 15],
    [4, 7, 7],
    [5, 10, 19]
]
max_days = 20
num_people = 5