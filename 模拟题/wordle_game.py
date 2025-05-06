from collections import Counter


class Solution:
    def wordle_game(self, guess, secret):
        n = len(guess)
        ans = ['' for _ in range(n)]

        cnt = Counter()
        for i in range(n):
            if guess[i] == secret[i]:
                ans[i] = 'G'
            else:
                cnt[secret[i]] += 1

        for i in range(n):
            if ans[i] == '':
                if cnt[guess[i]]:
                    ans[i] = 'Y'
                else:
                    ans[i] = 'R'
        return ''.join(ans)


print(Solution().wordle_game('BLAST', 'CHALK'))