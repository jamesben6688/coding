from collections import Counter

from collections import Counter


def can_split_into_groups(cards):
    # 统计每张牌出现的次数
    card_count = Counter(cards)

    # 创建一个列表，方便操作
    def can_form_groups(remaining_counts):
        # 如果没有剩余的牌，则已经成功分组
        if sum(remaining_counts.values()) == 0:
            return True

        # 获取所有未使用的数字（排序确保从小到大处理）
        for num in sorted(remaining_counts):
            if remaining_counts[num] > 0:
                # 尝试使用三张相同的牌
                if remaining_counts[num] >= 3:
                    remaining_counts[num] -= 3
                    if can_form_groups(remaining_counts):
                        return True
                    remaining_counts[num] += 3

                # 尝试使用三张连续的牌
                if remaining_counts[num] > 0 and remaining_counts.get(num + 1, 0) > 0 and remaining_counts.get(num + 2,
                                                                                                               0) > 0:
                    remaining_counts[num] -= 1
                    remaining_counts[num + 1] -= 1
                    remaining_counts[num + 2] -= 1
                    if can_form_groups(remaining_counts):
                        return True
                    remaining_counts[num] += 1
                    remaining_counts[num + 1] += 1
                    remaining_counts[num + 2] += 1

                # 如果都不行，则返回 False
                return False

        return False

    # 开始回溯，尝试不同的分组方式
    return can_form_groups(card_count)


# 示例
# cards = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8]
# print(can_split_into_groups(cards))  # 输出: False
#
# print(can_split_into_groups([1, 2, 3, 2, 3, 4, 3, 4, 5, 6, 7, 8]))  # True
# print(can_split_into_groups([1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8]))  # True
# print(can_split_into_groups([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6]))  # True
print(can_split_into_groups([1, 1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 8]))  # True [1, 1, 1] [2, 3 , 4] [3 4 5] 6 7 8]
