def merge_timeseries_sum(T1, T2):
    # 所有的变化时间点
    time_points = set([t for t, _ in T1] + [t for t, _ in T2])
    time_points = sorted(time_points)

    # 将原始序列变成 dict，方便查找
    t1_map = dict(T1)
    t2_map = dict(T2)

    result = []
    curr_val_t1 = 0
    curr_val_t2 = 0
    prev_total = None

    for t in time_points:
        if t in t1_map:
            curr_val_t1 = t1_map[t]
        if t in t2_map:
            curr_val_t2 = t2_map[t]
        total = curr_val_t1 + curr_val_t2
        if prev_total != total:
            result.append([t, total])
            prev_total = total

    return result
