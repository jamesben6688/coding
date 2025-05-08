from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """
            dp[i][j] = 1 + dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]
        """

        m = len(mat)
        n = len(mat[0])

        ans = 0
        for i in range(m):
            col = mat[i][:]

            for j in range(i, m):
                if j > i:
                    for k in range(n):
                        col[k] += mat[j][k]

                s = j + 1 - i

                """
                    count the number of sub-arr whose sum equals to s
                """
                cnt = 0

                right = 0
                while right < n:
                    if col[right] == s:
                        cnt += 1
                    else:
                        ans += cnt
                        cnt = 0
                    right += 1
                ans += cnt

        return ans


print(Solution().numSubmat(
    mat = [[1,0,1],[1,1,0],[1,1,0]]
))