ids = [
    "1234",
    "1235",
    "2234",
    "2235",
]
from collections import Counter

def min_positions_to_mask_two_groups(ids):
    m = len(ids)
    n = len(ids[0])

    must_mask = 0

    candidates = []
    for i in range(n):
        cnt = Counter()
        for j in range(m):
            cnt[ids[i][j]] += 1

        if len(cnt) > 2:
            must_mask += 1
        elif len(cnt) == 2:
            candidates.append(i)

    mx_cnt = 0
    from collections import defaultdict
    for i in range(len(candidates)):
        c = candidates[i]
        vals = defaultdict(list)
        for row in range(m):
            vals[ids[row][c]].append(row)

        values = [set(), set()]
        for j in range(len(candidates)):
            if j != i:
                for row in range(m):




print(min_positions_to_mask_two_groups(ids))  # 输出 1
