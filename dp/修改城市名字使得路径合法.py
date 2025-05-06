from collections import defaultdict


class Solution:
    def min_change(self, edges, path):
        def get_cost(a, b):
            assert len(a) == len(b), "length must the same"
            ans = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    ans += 1
            return ans

        g = defaultdict(list)
        cities_set = set()
        for a, b in edges:
            g[b].append(a)
            cities_set.add(a)
            cities_set.add(b)

        cities = list(cities_set)
        n = len(path)
        dp = defaultdict(lambda: defaultdict(lambda: [float('inf'), []]))

        for c in cities:
            dp[0][c] = [get_cost(path[0], c), [c]]

        for i in range(1, len(path)):
            for c in cities:
                for prev in g[c]:
                    if dp[i-1][prev][0] + get_cost(path[i], c) < dp[i][c][0]:
                        dp[i][c] = [dp[i-1][prev][0] + get_cost(path[i], c), dp[i-1][prev][1]+[c]]
                    # dp[i][c] = min(dp[i][c], get_cost(path[i], c)+dp[i-1][prev])

        cs = list(dp[n-1].keys())
        ans_city = cs[0]
        for c in range(1, len(cs)):
            if dp[n-1][c][0] < dp[n-1][ans_city][0]:
                ans_city = c
        return dp[n-1][ans_city]


        """
            dp[i][city] = min(dp[i-1][prev] + cost(path[i], city) and edges[prev][city] exists)
        
            dp: {
                2 :{city1 : 1, city2: 2}
            }
        """


print(Solution().min_change(
    [["ACC", "ABB"], ["ABB", "ABD"]], ["ACC", "ABD"]
))




