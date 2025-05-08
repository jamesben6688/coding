import random

class Maze:
    def __init__(self, size):
        """
            prim算法生成迷宫: https://blog.csdn.net/wxc971231/article/details/88217447
        :param size:
        """
        self.size = size
        self.maze = [[0 for _ in range(size)] for _ in range(size)]
        self.visited = [[0 for _ in range(size)] for _ in range(size)]

    def is_valid(self, x, y):
        return 0 < x < self.size - 1 and 0 < y < self.size - 1 and self.visited[x][y] == 0

    def generate_with_prim(self):
        class Cell:
            def __init__(self, x, y, next_x, next_y):
                self.x = x
                self.y = y
                self.next = (next_x, next_y)

        dir = [0, 1, 0, -1, 0]
        v = []
        x, y = 1, 1
        self.visited[x][y] = 1
        self.maze[x][y] = 1

        # 初始邻接墙加入列表
        for i in range(4):
            nx, ny = x + dir[i], y + dir[i + 1]
            if self.is_valid(nx, ny):
                self.visited[nx][ny] = 1
                next_x, next_y = nx + dir[i], ny + dir[i + 1]
                v.append(Cell(nx, ny, next_x, next_y))

        count = random.randint(0, 999)
        while v:  # 没有墙为止
            count += 1
            random.seed(count)
            pos = random.randint(0, len(v) - 1)  # 从集合总随机选择一个墙
            temp = v[pos]
            x, y = temp.next
            if self.is_valid(x, y):
                self.maze[temp.x][temp.y] = 1  # 打通墙
                self.maze[x][y] = 1
                self.visited[x][y] = 1
                for i in range(4):  # 把新的通道点四周的墙加入集合中, 知道没有墙为止
                    nx, ny = x + dir[i], y + dir[i + 1]
                    if self.is_valid(nx, ny):
                        self.visited[nx][ny] = 1
                        next_x, next_y = nx + dir[i], ny + dir[i + 1]
                        v.append(Cell(nx, ny, next_x, next_y))

            # 删除当前cell
            v.pop(pos)

    def __repr__(self):
        return '\n'.join(''.join('0' if cell else '#' for cell in row) for row in self.maze)


# 示例生成
maze = Maze(21)
maze.generate_with_prim()
print(maze)
