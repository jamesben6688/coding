import random

def generate_maze(m, n):
    # 初始化全是墙
    maze = [[1 for _ in range(n)] for _ in range(m)]

    def in_bounds(x, y):
        return 0 <= x < m and 0 <= y < n

    def carve(x, y):
        maze[x][y] = 0
        dirs = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and maze[nx][ny] == 1:
                maze[x + dx // 2][y + dy // 2] = 0  # carve wall between
                carve(nx, ny)

    # 确保行列为奇数，迷宫才是对称完整的
    if m % 2 == 0: m += 1
    if n % 2 == 0: n += 1

    carve(1, 1)  # 从(1,1)开始挖通

    # 起点终点
    maze[1][0] = 0  # Start
    maze[m-2][n-1] = 0  # End
    return maze

# 打印函数
def print_maze(maze):
    for row in maze:
        print("".join("O" if cell == 1 else " " for cell in row))

# 示例
maze = generate_maze(15, 25)
print_maze(maze)
