"""
1. 从给定的坐标(x, y) 出发, 用floodfill算法将所有的陆地的格子存入到一个set中。
"""
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右方向


def is_valid(x, y, ocean, visited):
    """检查坐标(x, y)是否在合法范围内，并且该位置尚未被访问过"""
    return 0 <= x < len(ocean) and 0 <= y < len(ocean[0]) and ocean[x][y] == 'x' and (x, y) not in visited


def flood_fill_land(ocean, x, y, visited):
    """Flood fill 从给定坐标 (x, y) 开始，找到所有的陆地并存入到 set 中"""
    stack = [(x, y)]
    visited.add((x, y))  # 记录已访问过的格子
    land_cells = set()  # 用于存储所有的陆地格子

    while stack:
        cx, cy = stack.pop()
        land_cells.add((cx, cy))  # 将当前格子加入陆地集合

        # 遍历四个方向
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny, ocean, visited):
                visited.add((nx, ny))
                stack.append((nx, ny))

    return land_cells


# 示例
ocean = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "x", "x", ".", ".", ".", "x", ".", ".", ".", "."],
    [".", "x", ".", ".", ".", "x", ".", "x", ".", ".", "."],
    [".", ".", ".", ".", ".", "x", ".", "x", ".", ".", "."],
    [".", "x", "x", "x", ".", "x", "x", "x", ".", ".", "."],
    [".", "x", ".", "x", ".", "x", ".", "x", ".", ".", "."],
    [".", "x", "x", "x", ".", "x", ".", "x", "x", ".", "."],
    [".", ".", ".", ".", ".", "x", ".", ".", "x", ".", "."],
    [".", ".", ".", ".", ".", "x", "x", "x", "x", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
]

point = (1, 1)  # 假设从 (1, 1) 开始

# 创建一个访问过的集合
visited = set()

# 获取所有陆地格子
land_cells = flood_fill_land(ocean, point[0], point[1], visited)
print(land_cells)

"""
第2步, 根据这些陆地的cell, 人为构造一个更小的矩形框, 最外面一层是水。然后里面就是原来的岛屿和水域, 从而缩小搜索面积。
"""


def construct_subgrid(ocean, land_cells):
    """根据陆地格子，构造一个更小的矩形框"""
    if not land_cells:
        return []

    # 找到陆地格子的最小和最大 x 和 y 坐标
    min_x = min(cell[0] for cell in land_cells)
    max_x = max(cell[0] for cell in land_cells)
    min_y = min(cell[1] for cell in land_cells)
    max_y = max(cell[1] for cell in land_cells)

    # 构建新的子网格，大小为 (max_x - min_x + 3) x (max_y - min_y + 3)
    # 外围一层水域，再加上原始的岛屿和水域
    subgrid = [['.'] * (max_y - min_y + 3) for _ in range(max_x - min_x + 3)]

    # 将原始的岛屿和水域映射到新的子网格
    for x, y in land_cells:
        new_x = x - min_x + 1  # 使得最小的 x 对应子网格的第一个位置
        new_y = y - min_y + 1  # 使得最小的 y 对应子网格的第一个位置
        subgrid[new_x][new_y] = 'X'

    # 返回构造好的子网格
    return subgrid


# 示例
ocean = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "x", "x", ".", ".", ".", "x", ".", ".", ".", "."],
    [".", "x", ".", ".", ".", "x", ".", "x", ".", ".", "."],
    [".", ".", ".", ".", ".", "x", ".", "x", ".", ".", "."],
    [".", "x", "x", "x", ".", "x", "x", "x", ".", ".", "."],
    [".", "x", ".", "x", ".", "x", ".", "x", ".", ".", "."],
    [".", "x", "x", "x", ".", "x", ".", "x", "x", ".", "."],
    [".", ".", ".", ".", ".", "x", ".", ".", "x", ".", "."],
    [".", ".", ".", ".", ".", "x", "x", "x", "x", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
]

# 假设从 (1, 1) 开始，得到陆地的集合
land_cells = flood_fill_land(ocean, 1, 1, set())

# 构建新的子网格
subgrid = construct_subgrid(ocean, land_cells)

# 打印新的子网格
for row in subgrid:
    print(''.join(row))

"""
第三步, 对于新的子网格, 从有水的格子开始, 用洪水填充算法。如果最终碰到了边界, 则表明是属于海洋, 不是湖泊。如果最终都没有碰到边界, 则表明是一个内部湖泊, 湖泊数量加一。然后将以上遍历过程中所有岛屿对应的湖泊数量用一个哈希表存起来, 方便后面如果碰到了可以直接返回。
"""


def flood_fill_water(ocean, x, y, visited, is_ocean=False):
    """Flood fill 算法，判断该水域是否属于海洋。如果与边界接触，则是海洋。"""
    stack = [(x, y)]
    visited.add((x, y))
    water_cells = set()

    while stack:
        cx, cy = stack.pop()
        water_cells.add((cx, cy))

        # 如果当前格子触及边界，则是海洋
        if cx == 0 or cx == len(ocean) - 1 or cy == 0 or cy == len(ocean[0]) - 1:
            is_ocean = True

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny, ocean, visited) and ocean[nx][ny] == ".":
                visited.add((nx, ny))
                stack.append((nx, ny))

    return water_cells, is_ocean


def count_lakes_in_subgrid(ocean, land_cells):
    """ 在缩小的矩阵内计算湖泊的数量 """
    visited = set()
    lakes = 0
    island_lake_map = {}  # 用于缓存每个岛屿的湖泊数量

    # 对每个水域格子进行洪水填充，检查是否是湖泊
    for x in range(1, len(ocean) - 1):
        for y in range(1, len(ocean[0]) - 1):
            if ocean[x][y] == "." and (x, y) not in visited:
                # 使用洪水填充检查这个水域是否是海洋
                water_cells, is_ocean = flood_fill_water(ocean, x, y, visited, is_ocean=False)

                if is_ocean:
                    # 如果是海洋，不计入湖泊
                    continue
                else:
                    # 如果不是海洋，就是湖泊
                    lakes += 1

                # 将所有水域标记为已访问
                visited.update(water_cells)

    return lakes


# 示例
ocean = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "x", "x", ".", ".", ".", "x", ".", ".", ".", "."],
    [".", "x", ".", ".", ".", "x", ".", "x", ".", ".", "."],
    [".", ".", ".", ".", ".", "x", ".", "x", ".", ".", "."],
    [".", "x", "x", "x", ".", "x", "x", "x", ".", ".", "."],
    [".", "x", ".", "x", ".", "x", ".", "x", ".", ".", "."],
    [".", "x", "x", "x", ".", "x", ".", "x", "x", ".", "."],
    [".", ".", ".", ".", ".", "x", ".", ".", "x", ".", "."],
    [".", ".", ".", ".", ".", "x", "x", "x", "x", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
]

# 假设从 (1, 1) 开始，得到陆地的集合
land_cells = flood_fill_land(ocean, 1, 1, set())

# 构建新的子网格
subgrid = construct_subgrid(ocean, land_cells)

# 计算湖泊的数量
lakes = count_lakes_in_subgrid(subgrid, land_cells)
print(f"湖泊数量：{lakes}")
