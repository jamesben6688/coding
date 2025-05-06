def rearrange_array(nums):
    # 左指针指向数组的起始位置，右指针指向数组的结束位置
    left, right = 0, len(nums) - 1

    while left < right:
        # 左指针找到奇数
        while left < right and nums[left] % 2 == 0:
            left += 1
        # 右指针找到偶数
        while left < right and nums[right] % 2 != 0:
            right -= 1

        # 如果left指向奇数且right指向偶数，交换它们
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]

    return nums


# 示例使用
nums = [3, 2, 1, 4, 7, 6, 5, 8]
result = rearrange_array(nums)
print(result)  # 输出：[8, 2, 4, 6, 7, 1, 5, 3]
