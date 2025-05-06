class Solution:
    def rearrange(self, nums):
        def dfs(arr):
            if len(arr) <= 1:
                return arr

            arr_odd = arr[0::2]
            arr_even = arr[1::2]

            arr_odd = dfs(arr_odd)
            arr_even = dfs(arr_even)

            return arr_odd + arr_even

        return dfs(nums)


print(Solution().rearrange([x for x in range(10)]))
