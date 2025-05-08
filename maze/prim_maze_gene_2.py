import random

class Maze:
    def __init__(self, size):
        self.size = size
        self.num_call = 0
        self.wall_ch = '#'
        self.space_ch = '·'
        self.maze = [[self.wall_ch] * size for _ in range(size)]
        self.forest = []
        self.points = []
        self.start = [1, 1]
        self.end = [self.size-2, self.size-2]
        for i in range(1, size, 2):
            for j in range(1, size, 2):
                self.maze[i][j] = self.space_ch
                self.forest.append([[i, j]])
                self.points.append([i, j])

        print(self)
        print("=" * 20)
        while len(self.forest) > 2:
            for pos in self.points:
                self.break_wall(pos)

    def __repr__(self):
        ans = []
        for i in range(self.size):
            ans.append("".join(self.maze[i]))
        return "\n".join(ans)

    def break_wall(self, pos):
        ranlist = [1, 2, 3, 4]
        start_tree = []
        connected_tree = []
        tar = []
        for tree in self.forest:
            if pos in tree:
                start_tree = tree
                break
        if len(self.forest) == 1:
            return

        if pos[0] < 2 or [pos[0] - 2, pos[1]] in start_tree:
            ranlist.remove(1)
        if pos[1] < 2 or [pos[0], pos[1] - 2] in start_tree:
            ranlist.remove(2)
        if pos[0] > self.size - 3 or [pos[0] + 2, pos[1]] in start_tree:
            ranlist.remove(3)
        if pos[1] > self.size - 3 or [pos[0], pos[1] + 2] in start_tree:
            ranlist.remove(4)

        direction = random.choice(ranlist)
        if direction == 1:
            self.maze[pos[0]-1][pos[1]] = self.space_ch
            tar = [pos[0] - 2, pos[1]]
        elif direction == 2:
            self.maze[pos[0]][pos[1] - 1] = self.space_ch
            tar = [pos[0], pos[1] - 2]
        elif direction == 3:
            self.maze[pos[0] + 1][pos[1]] = self.space_ch
            tar = [pos[0] + 2, pos[1]]
        elif direction == 4:
            self.maze[pos[0]][pos[1]+1] = self.space_ch
            tar = [pos[0], pos[1] + 2]

        for tree in self.forest:
            if tar in tree:
                connected_tree = tree
                break

        start_tree.extend(connected_tree)
        self.forest.remove(connected_tree)

    def find_neighbors(self, pos):
        nei = []
        for nextp in [[pos[0] - 1, pos[1]], [pos[0], pos[1]-1], [pos[0] + 1, pos[1]], [pos[0], pos[1] + 1]]:
            if self.maze[nextp[0]][nextp[1]] == self.space_ch:
                nei.append(nextp)
        return nei

maze = Maze(7)
print(maze)
