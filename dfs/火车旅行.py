from collections import defaultdict


class Solution:
    def can_arrive(self, trains, start_city, target_city):
        graph = defaultdict(defaultdict)
        path = []
        for d_time, a_time, s_city, e_city in trains:
            if e_city not in graph[s_city]:
                graph[s_city].update({e_city: [[d_time, a_time]]})
            else:
                graph[s_city][e_city].append([d_time, a_time])

        visited = set()
        visited.add(start_city)
        """
            {
                A: {
                        C: [[800, 900]],
                        E: [[900, 950]]
                    }
                C: {
                        
                    }
            }
        """
        mn_time = float('inf')
        ans = []
        from copy import deepcopy
        def dfs(city, a_time):
            nonlocal mn_time, ans
            if city == target_city:
                if a_time < mn_time:
                    mn_time = a_time
                    ans = deepcopy(path[:])
                return True
            for nxt_city in graph[city]:
                nxt_trains = graph[city][nxt_city]
                for d_time, a1_time in nxt_trains:
                    if a_time <= d_time and nxt_city not in visited:
                        visited.add(nxt_city)
                        path.append((nxt_city, d_time, a1_time))
                        dfs(nxt_city, a1_time)
                        visited.remove(nxt_city)
                        path.pop()
            return False
        path.append(start_city)
        dfs(start_city, 0)
        return ans



print(Solution().can_arrive(
trains = [
    (800, 900, "A", "C"),
    (910, 1000, "C", "D"),
    (1010, 1180, "D", "B"),
    (900, 950, "A", "E"),
    (960, 1100, "E", "B"),
    (850, 1200, "A", "B")  # 直接到但慢
],

start_city = "A",
target_city = "B"
))

print(Solution().can_arrive(
trains = [
    (1300, 1400, "A", "C"),
    (1450, 1500, "C", "B")  # 太早，赶不上
],
start_city = "A",
target_city = "B",
# ✅ 期望结果: 无法到达

))

