"""
规则 1：连续点数，不管花色, 至少 3 张牌

点数必须是连续的，比如 3-4-5-6
花色不影响
不允许循环，例如 "Q-K-A" 不是连续

规则 2：相同点数 + 相同花色
        至少 3 张牌

每张牌的点数和花色必须都相同（比如 3 张 "9D"）
"""


from collections import defaultdict

def is_valid_play(cards):
    if len(cards) < 2:
        return False

    rank_map = {
        '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    # 提取点数和花色
    rank_values = []
    card_count = defaultdict(int)  # 统计每张牌（点数+花色）出现次数

    for card in cards:
        rank = card[:-1]
        suit = card[-1]
        if rank not in rank_map:
            return False
        value = rank_map[rank]
        rank_values.append(value)
        card_count[card] += 1

    # ------- 检查是否存在 ≥3 连续的点数 -------
    unique_ranks = sorted(set(rank_values))
    for i in range(len(unique_ranks) - 2):
        if (unique_ranks[i+1] == unique_ranks[i] + 1 and
            unique_ranks[i+2] == unique_ranks[i] + 2):
            return True

    # ------- 检查是否存在某张牌出现 ≥3 次 -------
    for count in card_count.values():
        if count >= 3:
            return True

    return False



print(is_valid_play(["2D","4H", "6S", "3C"]))           # True，连续点数 2-3-4-6 ❌（错了）
print(is_valid_play(["3D", "3C", "3H", "6S"]))          # False，不同花色的相同点数，不行
print(is_valid_play(["3D", "4D", "7S", "6C", "10D", "9S"])) # False，完全乱
print(is_valid_play(["3D", "3D", "4S", "9D","9D"]))     # False，没有满足任意规则
print(is_valid_play(["3D", "3D", "9D", "4S", "9D","9D"]))# ✅ True，3张“9D”满足规则2
