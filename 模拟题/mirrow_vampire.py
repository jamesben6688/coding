"""
在一个2d空间中，有一些Vampire和mirror，input是这些vampire和镜子的row, column 坐标和镜子方向（东南西北），
设定是vampire在同一行或同一列面对自己的镜子中看到自己会embarrassed。 要求return 所有embarrassed vampire的
坐标以及embarrassed的方向。比如如果vampire在左边的镜子中看到自己，embarrassed方向就是西边。
vampire对同类来说是透明的。如果面向vampire的镜子被另一面相反方向的镜子挡住vampire就不会看到自己。
"""
from collections import defaultdict
import bisect

def find_embarrassed_vampires_fast(vampires, mirrors, rows, cols):
    vampire_set = set((r, c) for r, c in vampires)
    mirror_map = dict()
    for r, c, d in mirrors:
        mirror_map[(r, c)] = d

    embarrassed = defaultdict(set)

    # For each row/col, keep sorted list of vampires and mirrors
    row_map = defaultdict(lambda: {'v': [], 'm': []})
    col_map = defaultdict(lambda: {'v': [], 'm': []})

    for r, c in vampire_set:
        row_map[r]['v'].append(c)
        col_map[c]['v'].append(r)
    for (r, c) in mirror_map:
        row_map[r]['m'].append(c)
        col_map[c]['m'].append(r)

    # Sort them
    for r in row_map:
        row_map[r]['v'].sort()
        row_map[r]['m'].sort()
    for c in col_map:
        col_map[c]['v'].sort()
        col_map[c]['m'].sort()

    opp = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    direction_info = {
        'N': (col_map, -1, 'v', 'm', lambda lst, x: bisect.bisect_left(lst, x) - 1, 'S'),
        'S': (col_map, 1, 'v', 'm', lambda lst, x: bisect.bisect_right(lst, x), 'N'),
        'W': (row_map, -1, 'v', 'm', lambda lst, x: bisect.bisect_left(lst, x) - 1, 'E'),
        'E': (row_map, 1, 'v', 'm', lambda lst, x: bisect.bisect_right(lst, x), 'W'),
    }

    for (r, c), d in mirror_map.items():
        maps, step, vk, mk, finder, embarrass_dir = direction_info[d]

        idx = finder(maps[r if d in 'EW' else c][vk], c if d in 'EW' else r)
        m_idx = finder(maps[r if d in 'EW' else c][mk], c if d in 'EW' else r)

        # Check who appears first
        target_list = maps[r if d in 'EW' else c][vk]
        blocker_list = maps[r if d in 'EW' else c][mk]

        vampire_pos = target_list[idx] if 0 <= idx < len(target_list) else None
        mirror_pos = blocker_list[m_idx] if 0 <= m_idx < len(blocker_list) else None

        if vampire_pos is not None:
            if mirror_pos is None or \
               (step == 1 and vampire_pos < mirror_pos) or \
               (step == -1 and vampire_pos > mirror_pos):
                if d in 'NS':
                    embarrassed[(vampire_pos, c)].add(embarrass_dir)
                else:
                    embarrassed[(r, vampire_pos)].add(embarrass_dir)

    return sorted((r, c, sorted(list(dirs))) for (r, c), dirs in embarrassed.items())

vampires = [(2, 5), (4, 1), (5, 5), (6, 3), (3, 2)]
mirrors = [
    (0, 5, 'S'),  # 向下看到 (2, 5)
    (6, 3, 'W'),  # 向左不会看到任何 vampire（遇到自己）
    (4, 0, 'E'),  # 向右看到 (4, 1)
    (5, 6, 'W'),  # 向左看到 (5, 5)
    (2, 2, 'E'),  # 向右看到 (3, 2)
    (1, 5, 'S'),  # 向下看到 (2, 5)，但被 (2, 2) 拦住吗？不，因为不在一列
]

rows = 8
cols = 8


result = find_embarrassed_vampires_fast(vampires, mirrors, rows, cols)
for r, c, dirs in result:
    print(f"Vampire at ({r},{c}) is embarrassed from: {', '.join(dirs)}")
