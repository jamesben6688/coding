from collections import Counter


class Solution:
    """
        包含至少k个不同整数的最短连续子数组
    """
    def shortest_arr(self, nums, k):
        """
            考虑异常情况
        """
        if k > len(set(nums)):
            return -1

        cnt = Counter()
        left = 0
        n = len(nums)
        mn_len = len(nums)+1
        ans = []
        for i in range(n):
            cnt[nums[i]] += 1

            while len(cnt) >= k:
                if i+1-left < mn_len:
                    mn_len = i+1-left
                    ans = [nums[left:i+1]]
                elif i+1-left == mn_len:
                    ans.append(nums[left:i+1])

                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    cnt.pop(nums[left])
                left += 1

        return ans


print(Solution().shortest_arr(nums=[4, 3, 5, 3, 3, 1, 2, 3], k=3))
