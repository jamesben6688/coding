import heapq
from collections import Counter


def remove_k_largest_optimized(nums, k):
    if k == 0:
        return len(nums)

    # 找出最大的 k 个数
    k_largest = heapq.nlargest(k, nums)

    # 统计这 k 个数的出现次数（有可能有重复值）
    remove_counter = Counter(k_largest)

    # 遍历原数组，跳过这些要删除的数
    remaining = 0
    for num in nums:
        if num not in remove_counter:
            remaining += 1

    return remaining


print(remove_k_largest_optimized([0,1,2,3,3,3,4,5], 3))