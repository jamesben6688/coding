from typing import List

def balanced_substrings(strings, N):
    """
        贪心分配 O(N)

    :param strings:
    :param N:
    :return:
    """
    n = len(strings)
    lengths = [0] * n
    target = N // n

    # 初始分配
    for i in range(n):
        lengths[i] = min(len(strings[i]), target)

    used = sum(lengths)
    remaining = N - used

    # 贪心式地平均加1，直到用完预算
    while remaining > 0:
        updated = False
        for i in range(n):
            if lengths[i] < len(strings[i]):
                lengths[i] += 1
                remaining -= 1
                updated = True
                if remaining == 0:
                    break
        if not updated:
            break  # 已无法增加

    # 生成子串
    result = [s[:l] for s, l in zip(strings, lengths)]
    return result

strings = ["Embarcadero", "Ember", "SFO", "Montgomery"]
N = 7
print(balanced_substrings(strings, N))  # ➜ ["Em", "Em", "SF", "M"]
