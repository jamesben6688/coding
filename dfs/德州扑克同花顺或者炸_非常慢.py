"""
德州扑克: https://zh.wikipedia.org/wiki/%E6%92%B2%E5%85%8B%E7%89%8C%E5%9E%8B

check if the given 20 cards can be divided into 4 hands (Texas Holdem)
which are either royal flush or 4 of a kind.

Follow up to check if it will work by replacing only one card?
"""
# from itertools import combinations
# from collections import Counter
#
# def parse_card(card):
#     if card[:-1] == "10":
#         return "10", card[-1]
#     return card[:-1], card[-1]
#
# ROYAL_VALUES = {"10", "J", "Q", "K", "A"}
#
# def is_royal_flush(hand):
#     values = set()
#     suits = set()
#     for card in hand:
#         value, suit = parse_card(card)
#         values.add(value)
#         suits.add(suit)
#     return len(suits) == 1 and values == ROYAL_VALUES
#
# def is_four_of_a_kind(hand):
#     values = [parse_card(card)[0] for card in hand]
#     counter = Counter(values)
#     return 4 in counter.values()
#
# def valid_hand(hand):
#     return is_royal_flush(hand) or is_four_of_a_kind(hand)
#
# def can_form_4_valid_hands(cards):
#     all_valid_hands = []
#     card_indices = {card: i for i, card in enumerate(cards)}
#
#     # 所有可能的5张组合中，找出合法手牌
#     for combo in combinations(cards, 5):
#         if valid_hand(combo):
#             indices = set(card_indices[c] for c in combo)
#             all_valid_hands.append(indices)
#
#     # DFS 尝试从这些合法组合中找出 4 个互不相交的组合
#     def dfs(start, chosen):
#         if len(chosen) == 4:
#             return True
#         for i in range(start, len(all_valid_hands)):
#             hand = all_valid_hands[i]
#             if all(len(hand & c) == 0 for c in chosen):
#                 if dfs(i + 1, chosen + [hand]):
#                     return True
#         return False
#
#     return dfs(0, [])
#
# # 示例测试用例
# test_cases = [
#     ["AS", "KS", "QS", "JS", "10S",
#      "AH", "KH", "QH", "JH", "10H",
#      "AD", "KD", "QD", "JD", "10D",
#      "AC", "KC", "QC", "JC", "10C"],
#
#     ["AS", "AH", "AD", "AC", "2S",
#      "KS", "KH", "KD", "KC", "3S",
#      "QS", "QH", "QD", "QC", "4S",
#      "JS", "JH", "JD", "JC", "5S"],
#
#     ["AS", "KS", "QS", "JS", "10S",
#      "AH", "KH", "QH", "JH", "10H",
#      "AD", "KD", "QD", "JD", "10D",
#      "AC", "KC", "QC", "JC", "9C"],
#
#     ["AS", "AH", "AD", "AC", "2S",
#      "KS", "KH", "KD", "KC", "3S",
#      "QS", "QH", "QD", "QC", "4S",
#      "JS", "JH", "JD", "5S", "6S"],
#
#     ["2S", "3S", "4S", "5S", "6S",
#      "7H", "8H", "9H", "10H", "JH",
#      "QD", "KD", "AD", "2D", "3D",
#      "4C", "5C", "6C", "7C", "8C"]
# ]
#
# for i, cards in enumerate(test_cases):
#     print(f"测试用例 {i + 1}:")
#     if can_form_4_valid_hands(cards):
#         print("✅ 可分成 4 个合法手牌")
#     else:
#         print("❌ 无法分成 4 个合法手牌")
#     print("-" * 50)


def check_flush(cards):
    # 同花顺
    if len(cards) != 5:
        return False

    types = set([x[-1] for x in cards])
    if len(types) != 1:
        return False

    digits = []
    m = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    for x in cards:
        if len(x) == 3:
            digits.append(10)
        elif x[0] in m:
            digits.append(m[x[0]])
        else:
            digits.append(int(x[0]))

    digits = sorted(digits)
    for i in range(1, 5):
        if digits[i] - digits[i-1] != 1:
            return False
    # print('got a flush', cards)
    return True

def check_four_hand(cards):
    # 炸
    cnt = Counter([x[0] for x in cards])
    if len(cnt) != 2: return False

    for k in cnt:
        if cnt[k] == 1 or cnt[k] == 4:
            # print('get a four hand', cards)
            return True
    return False


from collections import Counter

def is_royal_flush(cards):
    suits = [card[-1] for card in cards]
    values = [card[:-1] for card in cards]
    return len(cards) == 5 and len(set(suits)) == 1 and set(values) == {"A", "K", "Q", "J", "10"}

def is_four_of_a_kind(cards):
    counts = Counter(card[:-1] for card in cards)
    return len(cards) == 5 and 4 in counts.values()

def can_split(cards):
    n = len(cards)
    if n != 20:
        return False

    cards = list(cards)

    def dfs(start, path, remaining, groups):
        if len(path) == 5:
            # 选了5张，看看是否合法
            if check_flush(path) or check_four_hand(path):
                if not remaining:
                    return len(groups) + 1 == 4
                return dfs(0, [], remaining, groups + [path])
            else:
                return False

        for i in range(0, len(remaining)):
            if dfs(i + 1, path + [remaining[i]], remaining[:i] + remaining[i+1:], groups):
                return True
        return False

    return dfs(0, [], cards, [])

# # 示例
# cards1 = [
#     "AS", "KS", "QS", "JS", "10S",
#     "AH", "AD", "AC", "AS", "5S",
#     "KH", "QH", "JH", "10H", "9H",
#     "9D", "9C", "9S", "9H", "2S"
# ]
#
# print(can_split(cards1))  # 输出 True


# from collections import Counter
#
#
# class TexasHoldem:
#     def is_valid(self, cards):
#         ans = []
#         path = []
#
#         def check_flush(cards):
#             # 同花顺
#             if len(cards) != 5:
#                 return False
#
#             types = set([x[-1] for x in cards])
#             if len(types) != 1:
#                 return False
#
#             digits = []
#             m = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
#             for x in cards:
#                 if len(x) == 3:
#                     digits.append(10)
#                 elif x[0] in m:
#                     digits.append(m[x[0]])
#                 else:
#                     digits.append(int(x[0]))
#
#             digits = sorted(digits)
#             for i in range(1, 5):
#                 if digits[i] - digits[i-1] != 1:
#                     return False
#             # print('got a flush', cards)
#             return True
#
#         def check_four_hand(cards):
#             # 炸
#             cnt = Counter([x[0] for x in cards])
#             if len(cnt) != 2: return False
#
#             for k in cnt:
#                 if cnt[k] == 1 or cnt[k] == 4:
#                     # print('get a four hand', cards)
#                     return True
#             return False
#
#         visited = [False] * len(cards)
#
#         def dfs(cur_idx):
#             # print(cur_idx)
#             nonlocal ans
#             if cur_idx == len(cards) and len(path) % 5 == 0:
#                 if len(path) > 0 and len(path) % 5 == 0 and not (check_flush(path[-5:]) or check_four_hand(path[-5:])):
#                     return False
#                 ans = path[:]
#                 return True
#
#             if len(path) > 0 and len(path) % 5 == 0 and not (check_flush(path[-5:]) or check_four_hand(path[-5:])):
#                 return False
#             # else:
#             for i in range(cur_idx, len(cards)):
#                 if not visited[i]:
#                     visited[i] = True
#                     path.append(cards[i])
#
#                     if dfs(cur_idx+1):
#                         return True
#
#                     visited[i] = False
#                     path.pop()
#             return False
#         # print(check_flush(ans), check_four_hand(ans))
#         return dfs(0), ans
#
#
print(can_split(
    [
        "AS", "KS", "QS", "JS", "9S",  # 错，缺了10S
        "AH", "AD", "AC", "KD", "5S",  # 错，混入了K
        "KH", "QH", "JH", "10H", "9H",  # ♥ Royal Flush
        "9D", "9C", "9S", "7D", "2S"  # 错，少一张9
    ]

))
#
#
