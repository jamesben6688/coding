class Solution:
    def max_customers(self, arr, init):
        left = 0
        mx = 0

        for i in range(len(arr)):
            init += arr[i]
            if init < 0:
                mx = max(mx, i-left)
                left = i+1
            elif i == len(arr)-1:
                mx = max(mx, i+1-left)

        return mx


print(Solution().max_customers([1, -3, 5, -2, 1], 1))
