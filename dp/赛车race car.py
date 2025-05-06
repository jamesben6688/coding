class Solution:
    def racecar(self, target: int) -> int:
        """
            nlg(N)

            打印最佳答案, 然后指令

        :param target:
        :return:
        """

        """
            dp[i] = dp[j] + steps(j, i)
        """

        dp = [[float('inf'), ""]] * (target + 1)

        As = 1
        ans = ""
        for i in range(1, target + 1):
            if i == (1 << As) - 1:
                dp[i] = [As, 'A' * As]
                # dp[i] =
                ans = 'A' * As
                As += 1
                continue

            if As + 1 + dp[(1 << As) - 1 - i][0] < dp[i][0]:
                dp[i] = (As + 1 + dp[(1 << As) - 1 - i][0], 'A' * As + 'R' + dp[(1 << As) - 1 - i][1])
                ans = dp[i]
            # dp[i] = min(dp[i][0], As+1+dp[(1<<As)-1-i])

            for back in range(1, As):
                # print(As-1, back-1)
                # pos = (1<<(As-1))-1 - ((1<<(back-1))-1)  #
                pos = (1 << (As - 1)) - 1 - ((1 << (back - 1)) - 1)
                if As - 1 + 1 + (back - 1) + 1 + dp[i - pos][0] < dp[i][0]:
                    dp[i] = (As - 1 + 1 + (back - 1) + 1 + dp[i - pos][0],
                             'A' * (As - 1) + 'R' + 'A' * (back - 1) + 'R' + dp[i - pos][1])
                # dp[i] = min(dp[i], As-1+1+(back-1)+1+dp[i-pos])

        print(dp[-1][1])
        return dp[-1][0]


