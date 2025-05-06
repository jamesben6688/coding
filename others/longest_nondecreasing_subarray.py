def max_increasing_subarr(arr):
    i = 0
    cur = 1
    ans = 1
    while i < len(arr):
        if i+1 < len(arr) and arr[i] <= arr[i+1]:
            cur += 1
        else:
            cur = 1
        ans = max(ans, cur)
        i += 1
    return ans



def maxIncreasingSubWithChange(arr):
    n = len(arr)
    if n <= 1:
        return n
    left = [1] * n  # left[i] is the max increasing subarray ending at i
    right = [1] * n  # right[i] is the max increasing subarray starting at i
    for pos in range(1, n):
        if arr[pos] >= arr[pos - 1]:
            left[pos] = left[pos - 1] + 1

    print(f"max len: {max(left)}")

    for pos in range(n - 2, -1, -1):
        if arr[pos] <= arr[pos + 1]:
            right[pos] = right[pos + 1] + 1

    max_res = max(left)
    for pos in range(1, n - 1):
        if arr[pos - 1] <= arr[pos + 1]:
            # [#We](https://leetcode.com/problems/power-of-two) consider changing the element at pos

            max_res = max(max_res, left[pos - 1] + right[pos + 1] + 1)

    # Consider changing the first element

    max_res = max(max_res, right[1] + 1)

    # Consider changing the last element
    max_res = max(max_res, left[n - 2] + 1)
    return max_res

print(max_increasing_subarr([0, 7, 3, 10, 2, 4, 6, 8, 0, 9, -20, 4]))
print(maxIncreasingSubWithChange([0, 7, 3, 10, 2, 4, 6, 8, 0, 9, -20, 4]))
