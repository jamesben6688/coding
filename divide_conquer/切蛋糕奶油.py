"""
 题目场景是有一个蛋糕，上面有一些长方形的奶油块。现在你要切这个蛋糕，
每一刀或平行或竖直（无斜刀）。并且贯穿，从一端到另外一端，也就是每一刀必定把你切的那块蛋糕
变成两块。不可以破坏奶油块。最终要求切出来的每块蛋糕上面都最多有一个奶油块，
求问能否有切法满足要求，如果有valid的切法最少几刀
"""

from functools import lru_cache


def min_cuts(cream_blocks):
    n = len(cream_blocks)

    # 把每个奶油块用索引表示，避免重复存储
    creams = list(range(n))

    @lru_cache(None)
    def dfs(block_indices):
        block_indices = tuple(sorted(block_indices))
        if len(block_indices) <= 1:
            return 0

        min_cut = float('inf')

        # 尝试所有水平切线（用奶油块的上边和下边之间的空隙）
        y_coords = []
        for idx in block_indices:
            y1, y2 = cream_blocks[idx][1], cream_blocks[idx][3]
            y_coords.append((y1, y2))

        y_cuts = get_valid_cuts(y_coords)
        for cut_y in y_cuts:
            upper = [i for i in block_indices if cream_blocks[i][1] >= cut_y]
            lower = [i for i in block_indices if cream_blocks[i][3] <= cut_y]
            if len(upper) + len(lower) == len(block_indices):  # 全部切开了
                cut_total = 1 + dfs(tuple(upper)) + dfs(tuple(lower))
                min_cut = min(min_cut, cut_total)

        # 尝试所有竖直切线（x 坐标）
        x_coords = []
        for idx in block_indices:
            x1, x2 = cream_blocks[idx][0], cream_blocks[idx][2]
            x_coords.append((x1, x2))

        x_cuts = get_valid_cuts(x_coords)
        for cut_x in x_cuts:
            left = [i for i in block_indices if cream_blocks[i][2] <= cut_x]
            right = [i for i in block_indices if cream_blocks[i][0] >= cut_x]
            if len(left) + len(right) == len(block_indices):
                cut_total = 1 + dfs(tuple(left)) + dfs(tuple(right))
                min_cut = min(min_cut, cut_total)

        return min_cut if min_cut != float('inf') else float('inf')

    def get_valid_cuts(intervals):
        # 从所有间隙中取中点作为切线
        coords = []
        for a, b in intervals:
            coords.append((a, 'start'))
            coords.append((b, 'end'))
        coords.sort()

        active = 0
        result = set()
        for i in range(1, len(coords)):
            typ1 = coords[i - 1][1]
            typ2 = coords[i][1]
            if typ1 == 'end':
                active -= 1
            if typ2 == 'start':
                active += 1
            if active == 0:
                mid = (coords[i - 1][0] + coords[i][0]) / 2
                result.add(mid)
        return result

    ans = dfs(tuple(creams))
    return ans if ans != float('inf') else -1


cream_blocks = [
    (1, 1, 2, 2),   # 奶油块 A
    (3, 1, 4, 2),   # 奶油块 B
    (1, 3, 2, 4),   # 奶油块 C
    (3, 3, 4, 4),   # 奶油块 D
]
print(min_cuts(cream_blocks))  # 输出 2：一刀水平一刀竖直