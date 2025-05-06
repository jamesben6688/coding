from bisect import bisect_left, bisect_right


def findMaxFrequency(nums):
    n = len(nums)
    if n == 0:
        return 0
    max_frequency = 0
    i = 0
    while i < n:
        # 使用二分查找找到当前数字的范围
        num = nums[i]
        left = bisect_left(nums, num)
        right = bisect_right(nums, num) - 1
        max_frequency = max(max_frequency, right - left + 1)
        i = right + 1  # 跳过当前块
    return max_frequency


print(findMaxFrequency([1,2,2,3,3,3,3,4,4,5,6]))
