# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot:
    def __init__(self, room):
        """
        初始化机器人，假设房间是一个二维网格，`room` 是一个二维列表，
        1 表示可以走的地方，0 表示障碍物。
        初始时机器人位于 (0, 0) 位置，朝向上方 (0, -1)。
        """
        self.room = room  # 房间（二维网格）
        self.x, self.y = 0, 0  # 初始位置
        self.directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 右, 上, 左, 下
        self.dir = 1  # 初始方向是上 (上为 1)

    def move(self):
        """
        移动机器人一个单位，如果可以移动到目标位置（不碰到障碍物），返回 True。
        否则返回 False，保持当前位置不变。
        """
        dx, dy = self.directions[self.dir]  # 获取当前方向的增量
        new_x, new_y = self.x + dx, self.y + dy

        # 检查目标位置是否在房间内且没有障碍物
        if 0 <= new_x < len(self.room) and 0 <= new_y < len(self.room[0]) and self.room[new_x][new_y] == 1:
            # 可以移动
            # self.x, self.y = new_x, new_y
            return True
        return False

    def turnLeft(self):
        """
        将机器人左转 90 度。
        """
        self.dir = (self.dir + 1) % 4  # 逆时针旋转，方向加 1，取模 4 确保在 0-3 之间

    def turnRight(self):
        """
        将机器人右转 90 度。
        """
        self.dir = (self.dir - 1) % 4  # 顺时针旋转，方向减 1，取模 4 确保在 0-3 之间

    def clean(self):
        """
        清扫当前单元格。
        """
        print(f"Cleaned cell at ({self.x}, {self.y})")  # 假设清扫时输出一个位置


class Direction:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    @staticmethod
    def turn_right(d):
        return (d + 1) % 4

# 移动方向数组：上、右、下、左
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Position:
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.direction = direction
        self.directions_used = 0

class Solution:
    def cleanRoom(self, robot):
        row, col = 0, 0
        direction = Direction.UP
        stack = [Position(row, col, direction)]
        in_stack = set()
        in_stack.add((row, col))

        while stack:
            pos = stack[-1]

            if pos.directions_used == 4:
                stack.pop()
                if stack:
                    # Turn back and move to previous position
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()
                continue

            robot.clean()

            d = pos.direction
            dx, dy = moves[d]
            next_row = pos.row + dx
            next_col = pos.col + dy

            if (next_row, next_col) not in in_stack and robot.move():
                next_pos = Position(next_row, next_col, d)
                stack.append(next_pos)
                in_stack.add((next_row, next_col))
            else:
                pos.directions_used += 1
                robot.turnRight()
                pos.direction = Direction.turn_right(pos.direction)



robot = Robot(
    [[1,1],
     [1,1]]
)

print(Solution().cleanRoom(robot))