class Solution:
    def score_student(self, scores):
        """
            leetcode 1996
        :param sores:
        :return:
        """
        scores = [(scores[i], i) for i in range(len(scores))]
        scores = sorted(scores, key=lambda x: (-x[0][0], x[0][1]))
        ans = [""] * len(scores)
        pre_max = -1
        for i in range(len(scores)):
            if scores[i][0][1] < pre_max:
                ans[scores[i][1]] = 'fail'
            else:
                ans[scores[i][1]] = 'pass'
                pre_max = scores[i][0][1]
        return ans


print(Solution().score_student([[1,5],[10,4],[4,3]]))
