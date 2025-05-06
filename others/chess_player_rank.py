from collections import defaultdict, deque


class Solution:
    def rank(self, wins, n):
        graph = defaultdict(list)

        indegrees = [0 for _ in range(n)]

        for a, b in wins:
            graph[a].append(b)
            indegrees[b] += 1

        que = deque()
        ans = []

        cur_rank = []
        for i in range(n):
            if indegrees[i] == 0:
                cur_rank.append(i)
                que.append(i)
        ans.append(cur_rank[:])
        cur_rank.clear()

        while que:
            q_size = len(que)
            for i in range(q_size):
                cur = que.popleft()

                for ne in graph[cur]:
                    indegrees[ne] -= 1
                    if indegrees[ne] == 0:
                        cur_rank.append(ne)
                        que.append(ne)

            ans.append(cur_rank[:])
            cur_rank.clear()

        return ans


print(Solution().rank([[0, 1], [2, 0]], n=3))




