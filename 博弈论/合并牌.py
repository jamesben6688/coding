from collections import Counter
from functools import lru_cache
from itertools import combinations


def can_combine(p1, p2):
    return len(p1) == len(p2) or p1[-1] == p2[-1]


def combine(p1, p2):
    return tuple(p1 + p2)


def canonical(state):
    return tuple(sorted(tuple(stack) for stack in state))


@lru_cache(None)
def can_win(state, turn):
    # state: tuple of stacks (each stack is a tuple of colors)
    stacks = list(state)
    n = len(stacks)

    for i in range(n):
        for j in range(i + 1, n):
            if can_combine(stacks[i], stacks[j]):
                # Try combining i and j
                new_stack = combine(stacks[i], stacks[j])
                new_state = stacks[:i] + stacks[i + 1:j] + stacks[j + 1:] + [new_stack]
                new_state_canon = canonical(new_state)
                if not can_win(new_state_canon, 1 - turn):
                    return True  # current player has a winning move
    return False  # no winning move


def can_perfect_win(player: int) -> bool:
    # Build initial state: 3 of each color
    colors = ['G'] * 3 + ['W'] * 3 + ['Y'] * 3 + ['B'] * 3
    initial_state = canonical([(c,) for c in colors])
    return can_win(initial_state, 0 if player == 1 else 1)


print(can_perfect_win(0))