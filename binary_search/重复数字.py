"""
用 pigeonhole 原理：统计 ≤ mid 的个数是否 > mid 来缩小区间
逻辑类似 “搜索数值” 而不是 index
"""
def find_duplicate_binary_search(nums):
    low, high = 1, len(nums) - 1  # 数值范围 [1, N]
    while low < high:
        mid = (low + high) // 2
        count = sum(num <= mid for num in nums)
        if count > mid:
            high = mid
        else:
            low = mid + 1
    return low


print(find_duplicate_binary_search([3,4,2,1,3]))