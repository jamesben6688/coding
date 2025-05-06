from collections import Counter, defaultdict
from itertools import combinations

def is_royal_flush(cards):
    """检查5张牌是不是 Royal Flush"""
    if len(cards) != 5:
        return False
    # 提取花色和点数
    suits = [card[-1] for card in cards]
    values = [card[:-1] for card in cards]
    # Royal flush必须是同一花色，且有 A, K, Q, J, 10
    return len(set(suits)) == 1 and set(values) == {"A", "K", "Q", "J", "10"}

def is_four_of_a_kind(cards):
    """检查5张牌是不是 Four of a Kind"""
    if len(cards) != 5:
        return False
    counts = Counter(card[:-1] for card in cards)  # 统计点数
    return 4 in counts.values()

def can_split(cards):
    """主函数"""
    if len(cards) != 20:
        return False

    cards = list(cards)

    def backtrack(remaining, groups):
        if not remaining:
            return len(groups) == 4
        # 每次从剩下的牌里选5张，组成一个group
        for comb in combinations(remaining, 5):
            comb_set = set(comb)
            if is_royal_flush(comb) or is_four_of_a_kind(comb):
                new_remaining = [c for c in remaining if c not in comb_set]
                if backtrack(new_remaining, groups + [comb]):
                    return True
        return False

    return backtrack(cards, [])


test_cases = [
    ["AS", "KS", "QS", "JS", "10S",
     "AH", "KH", "QH", "JH", "10H",
     "AD", "KD", "QD", "JD", "10D",
     "AC", "KC", "QC", "JC", "10C"],

    ["AS", "AH", "AD", "AC", "2S",
     "KS", "KH", "KD", "KC", "3S",
     "QS", "QH", "QD", "QC", "4S",
     "JS", "JH", "JD", "JC", "5S"],

    ["AS", "KS", "QS", "JS", "10S",
     "AH", "KH", "QH", "JH", "10H",
     "AD", "KD", "QD", "JD", "10D",
     "AC", "KC", "QC", "JC", "9C"],

    ["AS", "AH", "AD", "AC", "2S",
     "KS", "KH", "KD", "KC", "3S",
     "QS", "QH", "QD", "QC", "4S",
     "JS", "JH", "JD", "5S", "6S"],

    ["2S", "3S", "4S", "5S", "6S",
     "7H", "8H", "9H", "10H", "JH",
     "QD", "KD", "AD", "2D", "3D",
     "4C", "5C", "6C", "7C", "8C"]
]

# 示例
# cards1 = [
#     "AS", "KS", "QS", "JS", "10S",
#     "AH", "AD", "AC", "AS", "5S",
#     "KH", "QH", "JH", "10H", "9H",
#     "9D", "9C", "9S", "9H", "2S"
# ]

for cards1 in test_cases:
    print(can_split(cards1))  # 输出 True
