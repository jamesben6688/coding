class Solution:
    def get_min_lines(self, strs):
        words = strs.split(" ")
        """
            dp[i][j] 表示从s1[:i] 开始, s2[:j] 最少需要多少行
            
            dp[i-i1-1][j-j1-1] 表示从i s1[i-i1: i] ... s2[j-j1: j] in the same line
            dp[i][j] = 1 + dp[i-i1][j-j1] s.t. 
        """