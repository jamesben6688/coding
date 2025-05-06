class Solution:
    def max_num_of_1s(self, nums):
        mx_num = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                mx_num = max(mx_num, cnt)
            else:
                cnt = 0
        return mx_num


print(Solution().max_num_of_1s([1, 0, 1, 1, 1, 0]))