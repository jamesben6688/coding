def move_zero(nums):
    left = 0
    # [1 0 2 3]
    # [1 2 0 3]
    n = len(nums)
    i = j = 0
    while i < n and j < n:
        while i < n and nums[i] != 0:
            i += 1

        j = max(j, i+1)
        while j < n and nums[j] == 0:
            j += 1

        if i < n and j < n:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

    return nums


print(move_zero([1, 0, 2, 0, 3]))
