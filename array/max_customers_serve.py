class Solution:
    def max_customers(self, arr, init):
        """

        :param arr:
        :param init:
        :return:
        """
        left = 0
        mx = 0

        cnt = 0
        cur = init
        for item in arr:
            # mx = max(mx, cnt)

            cur += item
            cnt += 1

            if cur < 0:
                cur = init
                cnt = 0
            else:
                mx = max(mx, cnt)

        # for i in range(len(arr)):
        #     init += arr[i]
        #     if init < 0:
        #         mx = max(mx, i-left)
        #         left = i+1
        #     elif i == len(arr)-1:
        #         mx = max(mx, i+1-left)

        return mx


print(Solution().max_customers([1, -2, 5, -2, 1], 1))
