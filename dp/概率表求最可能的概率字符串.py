"""
Giving a table of probabilities P(a, b) = P(b | a),
write a function to find the m-letter word that is most likely generated.


"""


class Solution:
    def most_likely_word(self, P, P0, m):
        """
            dp[i][ch] = dp[i-1][c] * P[c][ch]

            followup: return that m-letter
        :param P0:
        :param P:
        :param m:
        :return:
        """
        chs = list(P0)
        n_chs = len(P0)
        dp = [[[0, '-']] * n_chs for _ in range(m)]
        for ch in P0:
            dp[0][ord(ch)-ord('a')] = [P0[ch], ch]

        for i in range(1, m):
            for ch in P0:
                for prev_ch in P0:
                    if dp[i-1][ord(prev_ch)-ord('a')][0] * P[prev_ch][ch] > dp[i][ord(ch)-ord('a')][0]:
                        dp[i][ord(ch)-ord('a')] = [dp[i-1][ord(prev_ch)-ord('a')][0] * P[prev_ch][ch],
                                                   prev_ch]
                    # dp[i][ord(ch)-ord('a')] = max(dp[i-1][ord(prev_ch)-ord('a')] * P[prev_ch][ch],
                    #                               dp[i][ord(ch)-ord('a')]
        cur_ch = 'a'
        for ch in P0:
            if dp[-1][ord(ch)-ord('a')][0] > dp[-1][ord(cur_ch)-ord('a')][0]:
                cur_ch = ch

        ans = cur_ch

        for i in range(m-1, 00, -1):
            cur_ch = dp[i][ord(cur_ch)-ord('a')][1]
            ans = cur_ch + ans  # i-1

        return max(dp[-1]), ans


P = {
    'a': {'a': 0.1, 'b': 0.6, 'c': 0.3},
    'b': {'a': 0.4, 'b': 0.5, 'c': 0.1},
    'c': {'a': 0.3, 'b': 0.3, 'c': 0.4}
}
P0 = {'a': 0.5, 'b': 0.3, 'c': 0.2}  # 0.5*0.6*0.5*0.5*0.5=0.0375

"""
    m=5
    abbbb: # 0.5*0.6*0.5*0.5*0.5=0.0375
    babaa =0.3*0.4*0.6*0.4*0.1=0.00288
    
"""
print(Solution().most_likely_word(P, P0, 3))  # e.g.,
