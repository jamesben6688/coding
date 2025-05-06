"""

A Beautiful value means that the maximum streak of the specific item in the array.
Input:
1. an array with items.
2. target item
Output:
return the maximum streak
Follow up:
an array of targets items, please find its respective maximum streak.
"""

def beautiful_value(arr, target):
    max_streak = 0
    current = 0
    for item in arr:
        if item == target:
            current += 1
            max_streak = max(max_streak, current)
        else:
            current = 0
    return max_streak


def beautiful_values(arr, targets):
    targets = set(targets)  # 转为 set 加速查询
    streaks = {t: 0 for t in targets}
    current = {t: 0 for t in targets}

    for item in arr:
        for t in targets:
            if item == t:
                current[t] += 1
                streaks[t] = max(streaks[t], current[t])
            else:
                current[t] = 0
    return streaks
