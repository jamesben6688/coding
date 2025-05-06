from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m = len(board)
        n = len(board[0])
        visited = set()

        def dfs(x, y, d):
            if not 0 <= x < m: return 1
            if not 0 <= y < n: return 1
            if board[x][y] == '.': return 1

            visited.add((x, y))

            new_x = x + d[0]
            new_y = y + d[1]
            return dfs(new_x, new_y, d)

        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i, j) not in visited:
                    ans += 1
                    for d in dirs:
                        dfs(i, j, d)
        return ans


print(Solution().countBattleships(
[["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

))