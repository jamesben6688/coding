class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius


from collections import defaultdict


class Solution:
    def is_one_group(self, circles):
        graph = defaultdict(list)
        n = len(circles)
        visited = [False] * n
        def l2_distance_squre(circle_1, circle_2):
            return (circle_1.center_x - circle_2.center_x) ** 2 + (circle_1.center_y - circle_2.center_y) ** 2
        for i in range(n):
            for j in range(i+1, n):
                if l2_distance_squre(circles[i], circles[j]) <= (circles[i].radius + circles[j].radius) ** 2:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [0] * n
        def dfs(node):
            visited[node] = 1

            for ne in graph[node]:
                if not visited[ne]:
                    dfs(ne)

        dfs(0)
        return sum(visited) == n


print(Solution().is_one_group(
    # [Circle(0, 0, 3), Circle(4, 0, 3), Circle(2, 3, 2)],
    [Circle(0, 0, 5), Circle(0, 0, 3)],  # 期望输出: 同一组
    # [Circle(0, 0, 3), Circle(4, 0, 3),
    #  Circle(2, 3, 2), Circle(10, 10, 1)],  # 期望输出: 前三个同一组，第四个不同组
))