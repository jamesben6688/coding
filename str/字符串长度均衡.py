"""
from typing import List

def balanced_prefixes(strings: List[str], N: int) -> List[str]:
    m = len(strings)
    maxlens = [len(s) for s in strings]

    best = None  # (max-min, -total_used, [lengths])

    # total_chars: 从 N 递减找最优方案
    for total in range(N, -1, -1):
        base = total // m
        remainder = total % m

        # 初步分配：所有人 base
        lens = [min(base, maxlens[i]) for i in range(m)]

        # 计算目前已分配
        used = sum(lens)

        # 尝试再给一些人 +1，按谁还有空间排
        candidates = sorted(range(m), key=lambda i: (-(maxlens[i] - lens[i]), -maxlens[i]))
        idx = 0
        while used < total and idx < m:
            i = candidates[idx]
            if lens[i] < maxlens[i]:
                lens[i] += 1
                used += 1
            idx += 1

        if used == total:
            diff = max(lens) - min(lens)
            key = (diff, -total, lens)
            if best is None or key < best:
                best = key

    final_lens = best[2]
    return [strings[i][:final_lens[i]] for i in range(m)]

"""

from typing import List

def balanced_prefixes(strings: List[str], N: int) -> List[str]:
    m = len(strings)
    maxlens = [len(s) for s in strings]

    best = None  # (max-min, -total_used, [lengths])

    # total_chars: 从 N 递减找最优方案
    for total in range(N, -1, -1):
        base = total // m
        remainder = total % m

        # 初步分配：所有人 base
        lens = [min(base, maxlens[i]) for i in range(m)]

        # 计算目前已分配
        used = sum(lens)

        # 尝试再给一些人 +1，按谁还有空间排
        candidates = sorted(range(m), key=lambda i: (-(maxlens[i] - lens[i]), -maxlens[i]))
        idx = 0
        while used < total and idx < m:
            i = candidates[idx]
            if lens[i] < maxlens[i]:
                lens[i] += 1
                used += 1
            idx += 1

        if used == total:
            diff = max(lens) - min(lens)
            key = (diff, -total, lens)
            if best is None or key < best:
                best = key

    final_lens = best[2]
    return [strings[i][:final_lens[i]] for i in range(m)]
strings = ["Embarcadero", "Ember", "SFO", "Montgomery"]
N = 7
print(balanced_prefixes(strings, N))  # ➜ ["Em", "Em", "SF", "M"]
