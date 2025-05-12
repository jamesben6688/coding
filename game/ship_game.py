class BattleshipGame:
    def __init__(self, board):
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.shot = [[False] * self.n for _ in range(self.m)]
        self.ship_map = {}  # (i,j) ➝ ship_id
        self.ship_health = {}  # ship_id ➝ remaining hit points

        self._preprocess()

    def _preprocess(self):
        ship_id = 0
        visited = [[False] * self.n for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == 1 and not visited[i][j]:
                    cells = []
                    # check direction: horizontal or vertical
                    if j + 1 < self.n and self.board[i][j+1] == 1:
                        # horizontal ship
                        k = j
                        while k < self.n and self.board[i][k] == 1:
                            cells.append((i, k))
                            visited[i][k] = True
                            k += 1
                    elif i + 1 < self.m and self.board[i+1][j] == 1:
                        # vertical ship
                        k = i
                        while k < self.m and self.board[k][j] == 1:
                            cells.append((k, j))
                            visited[k][j] = True
                            k += 1
                    else:
                        # single-cell ship
                        cells.append((i, j))
                        visited[i][j] = True

                    # assign ship_id
                    for (x, y) in cells:
                        self.ship_map[(x, y)] = ship_id
                    self.ship_health[ship_id] = len(cells)
                    ship_id += 1

    def isShot(self, i, j):
        return self.shot[i][j]

    def shoot(self, i, j):
        if self.shot[i][j]:
            raise ValueError(f"Cell ({i}, {j}) has already been shot.")
        self.shot[i][j] = True

        if self.board[i][j] == 0:
            return "water"
        else:
            sid = self.ship_map[(i, j)]
            self.ship_health[sid] -= 1
            if self.ship_health[sid] == 0:
                return "sank"
            else:
                return "shot"
