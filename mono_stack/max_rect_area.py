"""

01矩阵求最大长方形面积。
"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        height = [0 for i in range(n+2)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j+1] += 1
                else:
                    height[j+1] = 0

            st = []

            st.append(0)
            for i in range(1, len(height)):
                while st and height[i] < height[st[-1]]:
                    last = st.pop()
                    if st:
                        ans = max(ans, height[last] * (i-st[-1]-1))

                st.append(i)

        return ans