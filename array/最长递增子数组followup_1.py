"""
最长递增子数组
"""


def maxIncreasingSubWithChange(arr):
    n = len(arr)
    if n <= 1:
        return n
    left = [1] * n  # left[i] is the max increasing subarray ending at i
    right = [1] * n  # right[i] is the max increasing subarray starting at i

    # 从左往右
    for pos in range(1, n):
        if arr[pos] >= arr[pos - 1]:
            left[pos] = left[pos - 1] + 1

    print(f"max len: {max(left)}")

    # 从右往左
    for pos in range(n - 2, -1, -1):
        if arr[pos] <= arr[pos + 1]:
            right[pos] = right[pos + 1] + 1

    max_res = max(left)
    # 修改pos[i]的值
    found = False
    for pos in range(1, n - 1):
        if arr[pos - 1] <= arr[pos + 1]:
            # [#We](https://leetcode.com/problems/power-of-two) consider changing the element at pos
            found = True
            max_res = max(max_res, left[pos - 1] + right[pos + 1] + 1)

    for pos in range(n-1):
        if arr[pos+1] < arr[pos]:
            max_res = max(max_res, left[pos]+1)

    # Consider changing the first element
    # 修改数组第一个值

    max_res = max(max_res, right[1] + 1)

    # Consider changing the last element
    # 修改数组最后一个值
    max_res = max(max_res, left[n - 2] + 1)
    return max_res


print(maxIncreasingSubWithChange([2, 4, 6, 8, 0, 7]))
