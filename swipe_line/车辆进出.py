from collections import defaultdict


def car_count_at_times(records, t):
    # 事件字典，记录每个时间点的增减
    events = defaultdict(int)

    # 处理所有车辆的进出时间
    for enter, exit in records:
        events[enter] += 1  # 车辆进入
        events[exit] -= 1  # 车辆退出

    # 计算从0到t每个时刻的车辆数
    result = []
    current_count = 0
    for time in range(t + 1):
        current_count += events[time]
        result.append(current_count)

    return result


# 示例
records = [[1, 6], [2, 9]]
t = 6
print(car_count_at_times(records, t))  # 输出 [0, 1, 2, 2, 2, 2, 1]
