from itertools import combinations
from functools import lru_cache

def can_combine(pile1, pile2):
    return len(pile1) == len(pile2) or pile1[-1] == pile2[-1]

def merge_piles(pile1, pile2):
    return pile1 + pile2

def normalize_state(piles):
    return frozenset(tuple(pile) for pile in piles)

def get_all_moves(state):
    piles = list(state)
    for i, j in combinations(range(len(piles)), 2):
        if can_combine(piles[i], piles[j]):
            new_pile = merge_piles(piles[i], piles[j])
            new_state = piles[:i] + piles[i+1:j] + piles[j+1:] + [new_pile]
            yield normalize_state(new_state)
        elif can_combine(piles[j], piles[i]):
            new_pile = merge_piles(piles[j], piles[i])
            new_state = piles[:j] + piles[j+1:i] + piles[i+1:] + [new_pile]
            yield normalize_state(new_state)

@lru_cache(maxsize=None)
def can_win(state, player_turn):
    moves = list(get_all_moves(state))
    if not moves:
        return False  # current player loses

    return any(not can_win(next_state, 1 - player_turn) for next_state in moves)

def has_perfect_play(starting_player=0):
    initial = ['G'] * 3 + ['W'] * 3 + ['Y'] * 3 + ['B'] * 3
    state = normalize_state([[c] for c in initial])
    return can_win(state, starting_player)
