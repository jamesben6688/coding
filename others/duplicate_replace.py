class Solution:
    def replace(self, nums):
        left = 0
        prev = 0
        nums.append(None)
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[left] = nums[i-1] * (i-prev)
                left += 1
                prev = i

        return nums[:left]


print(Solution().replace(nums=[1, 2, 2, 2, 3, 3, 5]))
