from typing import List
from collections import defaultdict


class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        ans = -1
        graph = defaultdict(lambda: defaultdict(int))
        for a, b in edges:
            graph[a].update({b: scores[b]})
            graph[b].update({a: scores[a]})

        ans_1 = None
        ans_2 = None
        # print(graph)
        for a, b in edges:
            if a==0 and b == 3:
                print(a, b)
            cur = scores[a] + scores[b]

            cur_max = cur
            ans_1 = None
            for ne in graph[a]:
                if ne != b:
                    cur_max = max(cur_max, cur + scores[ne])
                    ans_1 = ne

            if not ans_1:
                continue

            cur_max = cur
            ans_2 = None
            for ne in graph[b]:
                if ne != a and ne != ans_1:
                    cur_max = max(cur_max, cur + scores[ne])
                    ans_2 = ne

            if ans_2:
                ans = max(ans, cur + scores[ans_1] + scores[ans_2])

            print(a, b, ans_1, ans_2)

        # if ans_1 and ans_2:
        return ans


print(Solution().maximumScore(
scores =
[18,6,4,9,8,2],
edges =
[[0,1],[0,2],[0,3],[0,4],[0,5],[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]
))