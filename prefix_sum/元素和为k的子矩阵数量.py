from typing import List
from collections import Counter


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for i in range(m):
            col = matrix[i]
            for j in range(i, m):
                if j > i:
                    for k in range(n):
                        col[k] += matrix[j][k]

                cnt = Counter()

                prefix_sum = [0]
                for t in range(n):
                    prefix_sum.append(prefix_sum[-1]+col[t])

                for t in range(n+1):
                    if prefix_sum[t]-target in cnt:
                        ans += cnt[prefix_sum[t]-target]
                    cnt[prefix_sum[t]] += 1
        return ans


print(Solution().numSubmatrixSumTarget(
[[0,1,0],[1,1,1],[0,1,0]],
target =
0
))