"""
最长递增子数组
"""
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


print(max_increasing_subarr([2, 4, 6, 8, 0, 9]))