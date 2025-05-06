from collections import Counter


class Solution:
    def shortest(self, nums, k):
        left = 0
        i = 0

        n = len(nums)
        cnt = Counter()

        min_len = float('inf')
        ans = []
        while i < n:
            cnt[nums[i]] += 1
            while len(cnt) >= k:
                if i+1-left < min_len:
                    min_len = i+1-left
                    ans = nums[left:i+1][:]
                elif i+1-left == min_len:
                    ans.append(nums[left:i+1][:])

                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    cnt.pop(nums[left])
                left += 1

            i += 1
        return ans


print(Solution().shortest(nums=[4, 3, 5, 3, 3, 1, 2, 3], k=3))
