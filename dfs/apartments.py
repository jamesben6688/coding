from collections import defaultdict
from functools import cache
from pprint import pprint


def get_best_match(apartments, people):
    """

        有n个人, 每个人有(1+m)种选择, 共(1+m)^n
    :param apartments:
    :param people:
    :return:
    """
    apartments = list(apartments.values())
    people = list(people.values())
    m = len(apartments)
    n = len(people)
    used = [0] * n
    ans = [0] * n
    match = [-1] * n
    ans_match = []
    lived = [0] * m
    memo = defaultdict()
    def dfs(i):
        nonlocal ans, used, ans_match
        if i == len(people):
            if sum(used) > sum(ans):
                ans = used[:]
                ans_match = [match[:]]
            elif sum(used) == sum(ans):
                ans_match.append(match[:])
            return
        if sum(used) + (n - i) < sum(ans):
            return
        for j in range(m):
            if people[i] == 'yes' and lived[j] < apartments[j]:
                lived[j] += 1
                used[i] = 1
                match[i] = j
                dfs(i+1)
                lived[j] -= 1
                used[i] = 0
                match[i] = -1
                assign = True
            elif people[i] == 'no' and lived[j] == 0:
                lived[j] = float('inf')
                used[i] = 1
                match[i] = j
                dfs(i+1)
                lived[j] = 0
                used[i] = 0
                match[i] = -1
                assign = True

        dfs(i + 1)


    dfs(0)
    return ans_match


apartments = {
    'apt1': 1,
    'apt2': 2,
    'apt3': 3,
    'apt4': 1
}


"""
    dp[i] = dp[i-1] + 
"""

# apartments = {
#     'apt1': 2,
#     'apt2': 3,
#     'apt3': 1,
#     'apt4': 4,
#     'apt5': 2,
#     'apt6': 1,
#     'apt7': 3,
# }



people = {
    'alice': 'no',  # 0
    'bob': 'no', # 3
    'charlie': 'yes',  # 1
    'david': 'yes',  # 1
    'eva': 'yes',  # 2
    'frank': 'yes',  # 2
    'grace': 'yes',  # 2
    'helen': 'no'  # -1
}

# people = {
#     'bob': 'yes',
#     'charlie': 'yes',
#     'eva': 'yes',
#     'grace': 'yes',
#     'helen': 'yes',
#     'judy': 'yes',
#     'ken': 'yes',
#     'mike': 'yes',
#     'nina': 'yes',
#     'oliver': 'yes',
#     'quincy': 'yes',
#     'rachel': 'yes',
#     'frank': 'no',
#     'alice': 'no',
#     'paul': 'no',
#     'lisa': 'no',
#     'ivan': 'no',
#     'david': 'no',
# }


pprint(get_best_match(apartments, people))