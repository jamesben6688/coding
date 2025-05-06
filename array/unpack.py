def unpack(arr):
    """
    Given an array representing run-length encoded values, write an iterator to unpack it.
    :param arr:
    :return:
    """
    ans = []
    i = 0
    while i < len(arr):
        ans += [arr[i+1]] * arr[i]
        i += 2
    return ans

print(unpack([1, 2, 3, 4, 1, 5]))

# [1, 2, 3, 4, 1, 5],  [2, 4, 4, 4, 5]
