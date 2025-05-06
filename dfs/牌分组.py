from collections import Counter

def can_form_groups_fast(cards):
    if len(cards) != 12:
        return False

    count = Counter(cards)

    groups = 0
    while sum(count.values()) > 0:
        made_group = False
        # 再尝试组成三个相同

        for num in range(1, 10):
            if count[num] >= 3:
                count[num] -= 3
                groups += 1
                made_group = True
                break

        if made_group:
            continue

        # 先尝试组成顺子（优先连续）
        for num in range(1, 8):  # 1~7 能组成 num,num+1,num+2
            if count[num] > 0 and count[num+1] > 0 and count[num+2] > 0:
                count[num] -= 1
                count[num+1] -= 1
                count[num+2] -= 1
                groups += 1
                made_group = True
                break

        if not made_group:
            return False

    return groups == 4


print(can_form_groups_fast([1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8]))  # True
print(can_form_groups_fast([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6]))  # True
print(can_form_groups_fast([1, 1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 8]))  # False
