class Solution:
    def countDigitOne(self, n: int) -> int:
        """
            abc d efg
                1 000

            n % base - d * base

            d == 0

            [d] = 1
            abc = 0~abc-1

            efg = 0~999

            d === 1:
             extra: 0~efg

            d > 1:
                0~abc
                0~999
        """
        base = 1
        ans = 0
        while base <= n:
            cur = (n//base)%10

            high = n // (base*10)
            low = n % base

            if cur == 0:
                ans += high*base
            elif cur == 1:
                ans += high*base + low+1
            else:
                ans += (high+1) * base
            base *= 10
        return ans


print(Solution().countDigitOne(13))