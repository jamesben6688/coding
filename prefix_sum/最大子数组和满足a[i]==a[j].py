from collections import defaultdict


class Solution:
    def get_maxsum(self, nums):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        m = defaultdict(list)
        for i in range(0, len(nums)):
            if len(m[nums[i]]) == 0:
                m[nums[i]] = [float('inf'), -float('inf')]  # min, max
            m[nums[i]][0] = min(m[nums[i]][0], prefix_sum[i+1])
            m[nums[i]][1] = max(m[nums[i]][1], prefix_sum[i+1])

        ans = -float('inf')

        for k, v in m.items():
            if len(v) >= 2:
                ans = max(ans, v[-1]-v[0] + k)
        return ans


print(Solution().get_maxsum([1, 2, 1, 3, 1, 2, 1]))


