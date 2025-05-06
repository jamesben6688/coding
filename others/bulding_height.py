"""
City makes a plan for buildings and parking lots on land. The land can be divided into equal sized tiles. Each tile is either a building or parking lot. The height difference between building/parking lots on two adjacent tiles is no more than one. The locations of parking lots on the land are fixed. Write a function to find what is the highest building can be planned. [Adjacency only includes left, right, up and down. Specifically diagonal is not considered - two tiles share an edge to be considered as adjacent]

Example 1
Input

- - -
- - -
- - P
Output: 4 with following arrangement

4 3 2
3 2 1
2 1 P

Example 2
Input

- - P
- - -
- - P
Output: 3 with following arrangement

2 1 P
3 2 1
2 1 P
"""
from collections import deque


class Solution:
    def get_height(self, lands):
        que = deque()
        m = len(lands)
        n = len(lands[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if lands[i][j] == 'P':
                    que.append((i, j))
                    visited.add((i, j))

        while que:
            q_size = len(que)
            for i in range(q_size):
                cur_i, cur_j = que.popleft()
                for di, dj in dirs:
                    new_i = cur_i + di
                    new_j = cur_j + dj

                    if 0 <= new_i < m and 0 <= new_j < n and lands[new_i][new_j] != 'P' and (new_i, new_j) not in visited:
                        visited.add((new_i, new_j))
                        que.append((new_i, new_j))
            ans += 1
        return ans-1


print(Solution().get_height(
    # ["---",
    #  "---",
    #  "--P"]
    [
        "--P",
        "---",
        "--P"
    ]
))
