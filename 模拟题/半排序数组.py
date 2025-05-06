"""
Given an array arr. Return True if it is an almost sorted array, and False if it's not.
arr is almost sorted if there is an element arr[i] such that the rest of the array are sorted.
i.e. arr[0] <= arr[1] <= ... <= arr[i-2] <= arr[i-1] <= arr[i+1] <= arr[i+2] <= ... <= arr[n-2] <= arr[n-1]
"""


class Solution:
    def __init__(self):
        pass

    def is_valid(self, nums):
        n = len(nums)

        if n <= 2:
            return True  # 对于长度小于等于 2 的数组，直接返回 True

        # 记录逆序对的位置
        count = 0

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                # 如果逆序对超过 1 对，直接返回 False
                if count > 1:
                    return False

                # 判断能否删除 nums[i] 或 nums[i+1] 来恢复顺序
                # 删除 nums[i]： nums[i-1] <= nums[i+1]
                # 删除 nums[i+1]： nums[i] <= nums[i+2]
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    continue
                if (i + 2 < n and nums[i] <= nums[i + 2]):
                    continue
                return False

        return True




class Solution_1:
    def __init__(self):
        pass

    def is_valid(self, nums):
        cnt = 1
        n = len(nums)
        if n == 1: return False
        if n == 2: return nums[0] > nums[1]

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                cnt -= 1

                if i == 0 or i == n-2:
                    pass
                else:
                    mx = max(nums[i], nums[i+1])
                    mn = min(nums[i], nums[i+1])
                    if nums[i-1] <= mx <= nums[i+2] or nums[i-1] <= mn <= nums[i+2]:
                        pass
                    else:
                        return False

                if cnt < 0:
                    return False

        return cnt == 0
# [5, 1, 2, 3, 4]
# ([1, 2, 10, 3, 4, 5]))
# 5, 4, 3, 2, 1
print(Solution().is_valid([1, 3.5, 10, 3.4, 6, 15]))