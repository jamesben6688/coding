class Solution:
    def get_key(self, updates, num):
        h_map = {}
        for k, v in updates:
            h_map[v] = k
        return h_map[num]

print(Solution().get_key([[1, 10],[2, 10], [1, 20]], 10))