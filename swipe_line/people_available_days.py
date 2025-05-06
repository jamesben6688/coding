def available_days(person_times, max_days, num_people):
    if len(person_times) == 0: return max_days
    cnt = num_people
    days = []
    left = 1
    for p, s, e in person_times:
        days.append([s, -1])
        days.append([e+1, 1])

    days = sorted(days, key=lambda x: (x[0], x[1]))
    avail_days = []
    if days[0][0] > left:
        avail_days.append([left, days[0][0]-1])
    left = days[0][0]
    found = False
    for d, action in days:
        cnt += action
        if cnt == num_people:
            found = True
            left = d
        elif found:
            avail_days.append([left, d-1])
            found = False

    if days[-1][0] <= max_days:
        avail_days.append([days[-1][0], max_days])
    return avail_days



person_times = [
    [1, 1, 1],
    [2, 20, 20],
    [3, 5, 15],
    [4, 7, 7],
    [5, 10, 19]
]
max_days = 20
num_people = 5
# 缺席天：1, 5-15, 7, 10-19, 20
# 可用天：2, 3, 4, 6, 8, 9, 16
# ✅ 预期输出：7


result = available_days(person_times, max_days, num_people)
print(f"Number of available days: {result}")


# 测试用例
# person_times = [
#     [1, 2, 4],  # person 1 is unavailable from day 2 to day 4
#     [2, 3, 5],  # person 2 is unavailable from day 3 to day 5
#     [3, 1, 6]  # person 3 is unavailable from day 1 to day 6
# ]
# max_days = 6
# num_people = 3
#
# result = available_days(person_times, max_days, num_people)
# print(f"Number of available days: {result}")
