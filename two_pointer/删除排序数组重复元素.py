class Solution:
    def del_dup(self, arr):
        left = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                pass
            else:
                arr[left] = arr[i]
                left += 1

        return arr[:left]

from sortedcontainers.sorteddict import SortedDict
print(Solution().del_dup([1, 1, 2, 2, 2, 3, 4]))
