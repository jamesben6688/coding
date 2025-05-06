def unpack(arr):
    ans = []
    i = 0
    while i < len(arr):
        ans += [arr[i+1]] * arr[i]
        i += 2
    return ans

print(unpack([1, 2, 3, 4, 1, 5]))

# [1, 2, 3, 4, 1, 5],  [2, 4, 4, 4, 5]
