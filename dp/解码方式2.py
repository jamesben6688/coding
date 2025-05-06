class Solution:
    def numDecodings(self, s: str) -> int:
        """
            if s[i] == '*':
                if s[i-1] == '0':
                    dp[i] = 9dp[i-1]
                elif s[i-1]

            if s[i] = '0':
                dp[i] = dp[i-2]
            elif s[i-1] == '0':
                dp[i] = dp[i-1]
            elif int(s[i-1:i+1]) > 26:
                dp[i] = dp[i-1]
            elif s[i] == '*':
                dp[i] =
            else:
                dp[i] = dp[i-1] + dp[i-2]
        """

        # @cache
        def get_nums(s):
            if s == "": return 1

            ans = 0
            if s[-1] == '*':
                for i in range(1, 10):
                    ans += get_nums(s[:-1] + str(i))
            elif len(s) == 1:
                ans += 1
            elif s[-2] == '*':
                for i in range(1, 10):
                    ans += get_nums(s[:-2] + str(i) + s[-1])
            elif s[-1] == '0':
                if int(s[-2]) >= 3:
                    return 0
                ans += get_nums(s[:-2])
            elif s[-2] == '0':
                ans += get_nums(s[:-1])

            elif int(s[-2:]) > 26:
                ans += get_nums(s[:-1])
            else:
                ans += get_nums(s[:-2]) + get_nums(s[:-1])
            return ans

        return get_nums(s)


print(Solution().numDecodings(
"*1*1*0"
))