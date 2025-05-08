import random

class DFSMaze:
    def __init__(self, size):
        """

            dfs生成迷宫
        :param size:
        """
        self.size = size
        self.maze = [[0 for _ in range(size)] for _ in range(size)]
        self.visited = [[0 for _ in range(size)] for _ in range(size)]

    def is_valid(self, x, y):
        return 0 < x < self.size - 1 and 0 < y < self.size - 1 and not self.visited[x][y]

    def generate(self):
        dir = [0, 1, 0, -1, 0]  # 四方向偏移
        stack = [(1, 1)]
        self.visited[1][1] = 1
        self.maze[1][1] = 1  # path
        count = random.randint(0, 999)

        while stack:
            x, y = stack[-1]
            have_push = False
            directions = [0, 1, 2, 3]
            random.seed(count)
            random.shuffle(directions)
            count += 1

            for i in directions:  # 从起点开始随机遍历4个方向, 每次找到一个合格的方向就开始下一步
                dx, dy = dir[i], dir[i + 1]
                nx, ny = x + dx * 2, y + dy * 2
                if self.is_valid(nx, ny):
                    self.visited[nx][ny] = 1
                    self.maze[x + dx][y + dy] = 1  # 打通墙
                    self.maze[nx][ny] = 1
                    stack.append((nx, ny))
                    have_push = True
                    break

            if not have_push:  # no way out, 死胡同, 回溯
                stack.pop()

    def __repr__(self):
        return '\n'.join(''.join('0' if cell else '#' for cell in row) for row in self.maze)


# 示例运行
maze = DFSMaze(21)
maze.generate()
print(maze)
