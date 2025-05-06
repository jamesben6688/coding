from typing import List



class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        indices = [[indices[i], i] for i in range(len(indices))]
        indices = sorted(indices)
        ans = ""
        n = len(indices)

        nxt_idx = 0
        for i in range(n):
            ss = sources[indices[i][1]]
            t = targets[indices[i][1]]

            idx = indices[i][0]

            ans += s[nxt_idx: idx]
            if s[idx:idx+len(ss)] == ss:
                ans += t
                nxt_idx = idx+len(ss)
            else:
                if i == len(indices)-1:
                    ans += s[idx:]
                    return ans
                else:
                    ans += s[idx:min(len(s), indices[i+1][0])]
                    nxt_idx = min(len(s), indices[i+1][0])
        ans += s[nxt_idx:]
        return ans


print(Solution().findReplaceString(
s =
"abcde",
indices =
[2,2,3],
sources =
["cde","cdef","dk"],
targets =
["fe","f","xyz"]
))