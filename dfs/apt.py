from itertools import product
from collections import defaultdict

# 示例数据
apartments = {
    'apt1': 2,
    'apt2': 3,
    'apt3': 1,
    'apt4': 4,
    'apt5': 2,
    'apt6': 1,
    'apt7': 3,
}


people = {
    'bob': 'yes',
    'charlie': 'yes',
    'eva': 'yes',
    'grace': 'yes',
    'helen': 'yes',
    'judy': 'yes',
    'ken': 'yes',
    'mike': 'yes',
    'nina': 'yes',
    'oliver': 'yes',
    'quincy': 'yes',
    'rachel': 'yes',
    'frank': 'no',
    'alice': 'no',
    'paul': 'no',
    'lisa': 'no',
    'ivan': 'no',
    'david': 'no',
}

person_list = list(people.keys())
apt_list = list(apartments.keys())
n = len(person_list)
m = len(apt_list)

apt_capacity = [apartments[apt] for apt in apt_list]

dp = defaultdict(dict)
initial_state = tuple(apt_capacity)
dp[0][initial_state] = {}

def try_assign(mask, state, person_idx, apt_idx, allow_sharing):
    new_state = list(state)
    if new_state[apt_idx] <= 0:
        return None
    rooms_used = sum(1 for p, a in dp[mask][state].items() if a == apt_list[apt_idx])
    if not allow_sharing and rooms_used > 0:
        return None
    new_state[apt_idx] -= 1
    return tuple(new_state)

# DP 主循环
for mask in range(1 << n):
    for state in dp[mask]:
        for i in range(n):
            if not (mask & (1 << i)):
                person = person_list[i]
                allow_sharing = people[person] == 'yes'
                for apt_idx in range(m):
                    new_state = try_assign(mask, state, i, apt_idx, allow_sharing)
                    if new_state is not None:
                        new_mask = mask | (1 << i)
                        if new_state not in dp[new_mask]:
                            dp[new_mask][new_state] = {}
                        new_assignment = dp[mask][state].copy()
                        new_assignment[person] = apt_list[apt_idx]
                        dp[new_mask][new_state] = new_assignment

# 找到安排人数最多的方案
max_people = -1
best_assignment = {}

for mask in dp:
    num_people = bin(mask).count('1')
    if num_people > max_people:
        for state in dp[mask]:
            max_people = num_people
            best_assignment = dp[mask][state]

# 输出结果
print("最多可入住人数:", max_people)
print("分配方案:", best_assignment)
