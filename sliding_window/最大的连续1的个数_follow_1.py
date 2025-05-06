class Solution:
    def max_num_of_1s(self, nums):
        mx_num = 0
        cnt = 0
        k = 1
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            mx_num = max(mx_num, i+1-left)

        return mx_num


print(Solution().max_num_of_1s([1, 0, 1, 1, 1, 0, 1, 1, 1]))