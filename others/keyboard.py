class Solution:
    def jump(self, keyboard, word, dis):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(keyboard)
        n = len(keyboard[0])

        def dfs(i, j, idx, step):
            if idx == len(word):
                return True

            if step <= 0: return False

            for d in range(4):
                ii = i + dirs[d][0]
                jj = j + dirs[d][1]
                if 0 <= ii < m and 0 <= jj < n:
                    if keyboard[ii][jj] == word[idx]:
                        if dfs(ii, jj, idx+1, dis):
                            return True
                    elif dfs(ii, jj, idx, step-1):
                        return True

            return False

        for i in range(m):
            for j in range(n):
                if keyboard[i][j] == word[0]:
                    if dfs(i, j, 1, dis):
                        return True
        return False


print(Solution().jump(
    [["Q", "X", "P", "L", "E"],
     ["W", "A", "C", "I", "N"]],
    'QPCW',
    2
))
