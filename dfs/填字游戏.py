from typing import List


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        word_len = len(word)

        def dfs(i, j, di, w_idx):
            if w_idx == word_len: return True

            if 0 <= i < m and 0 <= j < n and (board[i][j] == ' ' or board[i][j] == word[w_idx]):
                return dfs(i + dirs[di][0], j + dirs[di][1], di, w_idx + 1)
            else:
                return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == ' ' or board[i][j] == word[0]:
                    for di in range(4):
                        prev_i, prev_j = i - dirs[di][0], j - dirs[di][1]
                        if 0 <= prev_i < m and 0 <= prev_j < n and board[prev_i][prev_j] != '#':
                            continue

                        last_i = i + word_len * dirs[di][0]
                        last_j = j + word_len * dirs[di][1]

                        if 0 <= last_i < m and 0 <= last_j < n and board[last_i][last_j] != '#':
                            continue

                        if dfs(i, j, di, 0):
                            return True

        return False


print(Solution().placeWordInCrossword(
board =
[[" "," "],[" "," "]],
word =
"a"
))