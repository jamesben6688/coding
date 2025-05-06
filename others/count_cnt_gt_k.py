"""

第一道是easy大概就是统计每个数出现的次数是不是都大于一个值，

第二道是能不能把一个数组group成每五个连续的数
"""

from collections import Counter


def are_counts_greater_than_k(nums, k):
    # 统计每个数的出现次数
    count = Counter(nums)

    # 遍历字典，检查每个数的出现次数是否都大于 k
    for num, freq in count.items():
        if freq <= k:
            return False

    return True


# 示例输入
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
k = 2

# 调用函数
result = are_counts_greater_than_k(nums, k)
print(result)  # 输出: True，因为所有数字的出现次数都大于 2
