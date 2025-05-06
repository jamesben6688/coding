from typing import List, Tuple


def merge_schedule(schedule: List[Tuple[str, int, int]]):
    # 按开始时间排序
    schedule.sort(key=lambda x: x[1])  # 按开始时间排序

    ans = []

    cur = []
    t = []
    for item in schedule:
        t.append((item[0], item[1], 1))
        t.append((item[0], item[2], -1))

    t = sorted(t, key=lambda x: (x[1], -x[2]))

    prev_t = None
    for tt in t:
        if tt[2] > 0:
            if cur and tt[1] > prev_t:
                ans.append([prev_t, tt[1], cur[:]])
            cur.append(tt[0])
        else:
            if tt[1] > prev_t:
                ans.append([prev_t, tt[1], cur[:]])
            cur.remove(tt[0])
        prev_t = tt[1]
    return ans


# 示例
schedule = [
    ("Alice", 9, 12),  # Alice 9:00 - 12:00
    ("Bob", 10, 14),    # Bob 10:00 - 14:00
    ("Charlie", 11, 13),  # Charlie 11:00 - 13:00
    ("David", 13, 15),  # David 13:00 - 15:00
    ("Eve", 9, 11),  # Eve 9:00 - 11:00
]

result = merge_schedule(schedule)
for period in result:
    print(period)
