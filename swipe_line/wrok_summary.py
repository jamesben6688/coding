from pprint import pprint

def get_work_summary(schedule):
    t = []
    for s in schedule:
        t.append((s[0], s[1], 1))
        t.append((s[0], s[2], -1))

    t = sorted(t, key=lambda x: (x[1], x[2]))

    ans = []
    cur = set()
    prev_t = None
    for tt in t:
        """
            接下来人员会发生变化, 先收集上一次的结果
        """
        if cur and tt[1] > prev_t:
            ans.append([prev_t, tt[1], list(cur)])

        # 人员变化
        if tt[2] > 0:
            cur.add(tt[0])
        else:
            cur.remove(tt[0])

        prev_t = tt[1]

    return ans




schedule = [
    ("Alice", 9, 10),  # Alice 9:00 - 12:00
    ("Bob", 10, 14),    # Bob 10:00 - 14:00
    ("Charlie", 11, 13),  # Charlie 11:00 - 13:00
    ("David", 13, 15),  # David 13:00 - 15:00
    ("Eve", 9, 11),  # Eve 9:00 - 11:00
]

ans = get_work_summary(schedule)
pprint(ans)
