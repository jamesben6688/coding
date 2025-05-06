from itertools import combinations
from collections import Counter

def parse_card(card):
    if card[:-1] == "10":
        return "10", card[-1]
    return card[:-1], card[-1]

ROYAL_VALUES = {"10", "J", "Q", "K", "A"}
SUITS = "SHDC"
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def is_royal_flush(hand):
    values = set()
    suits = set()
    for card in hand:
        value, suit = parse_card(card)
        values.add(value)
        suits.add(suit)
    return len(suits) == 1 and values == ROYAL_VALUES

def is_four_of_a_kind(hand):
    values = [parse_card(card)[0] for card in hand]
    counter = Counter(values)
    return 4 in counter.values()

def valid_hand(hand):
    return is_royal_flush(hand) or is_four_of_a_kind(hand)

def can_form_4_valid_hands(cards):
    all_valid_hands = []
    card_indices = {card: i for i, card in enumerate(cards)}

    for combo in combinations(cards, 5):
        if valid_hand(combo):
            indices = set(card_indices[c] for c in combo)
            if len(indices) == 5:
                all_valid_hands.append(indices)

    def dfs(start, chosen):
        if len(chosen) == 4:
            return True
        for i in range(start, len(all_valid_hands)):
            hand = all_valid_hands[i]
            if all(len(hand & c) == 0 for c in chosen):
                if dfs(i + 1, chosen + [hand]):
                    return True
        return False

    return dfs(0, [])

def can_fix_by_replacing_one_card(cards):
    card_set = set(cards)
    for i in range(20):
        original_card = cards[i]
        for r in RANKS:
            for s in SUITS:
                new_card = r + s
                if new_card in card_set:
                    continue
                new_cards = cards[:i] + [new_card] + cards[i+1:]
                if can_form_4_valid_hands(new_cards):
                    return True
    return False

# 示例测试用例
test_cases = [
    ["AS", "KS", "QS", "JS", "10S",
     "AH", "KH", "QH", "JH", "10H",
     "AD", "KD", "QD", "JD", "10D",
     "AC", "KC", "QC", "JC", "10C"],  # ✅

    ["AS", "AH", "AD", "AC", "2S",
     "KS", "KH", "KD", "KC", "3S",
     "QS", "QH", "QD", "QC", "4S",
     "JS", "JH", "JD", "JC", "5S"],  # ✅

    ["AS", "KS", "QS", "JS", "10S",
     "AH", "KH", "QH", "JH", "10H",
     "AD", "KD", "QD", "JD", "10D",
     "AC", "KC", "QC", "JC", "9C"],   # 🔁

    ["AS", "AH", "AD", "AC", "2S",
     "KS", "KH", "KD", "KC", "3S",
     "QS", "QH", "QD", "QC", "4S",
     "JS", "JH", "JD", "5S", "6S"],   # 🔁

    ["2S", "3S", "4S", "5S", "6S",
     "7H", "8H", "9H", "10H", "JH",
     "QD", "KD", "AD", "2D", "3D",
     "4C", "5C", "6C", "7C", "8C"]    # ❌
]

for i, cards in enumerate(test_cases):
    print(f"测试用例 {i + 1}:")
    if can_form_4_valid_hands(cards):
        print("✅ 直接合法")
    elif can_fix_by_replacing_one_card(cards):
        print("🔁 替换一张牌后合法")
    else:
        print("❌ 无解")
    print("-" * 50)
