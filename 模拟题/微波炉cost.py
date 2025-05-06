class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        """
            分类讨论
        """

        def calc_cost(move: str) -> int:
            ans = 0
            cur = str(startAt)
            move = move.lstrip('0')
            for i in range(len(move)):
                if move[i] != cur:
                    ans += moveCost
                    cur = move[i]
                ans += pushCost
            return ans

        mins = targetSeconds // 60
        secs = targetSeconds % 60

        ans = float('inf')

        """
            1. < 60:
                only seconds
            2. >= 60:
                2.1 mins secs  s.t. mins < 100
                2.2 mins-1 secs + 60   s.t. secs+60 < 100
        """
        if mins == 0:
            ans = calc_cost(str(secs))
            return ans

        if secs < 40:
            ans = min(ans, calc_cost(str(mins - 1) + str(secs + 60)))

        if mins < 100:
            ans = min(ans, calc_cost(str(mins) + f"{secs:02}"))

        return ans

