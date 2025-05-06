import bisect

class Solution:
    def num_triplets_1(self, a, b, c, d):
        ans = 0
        for i in range(len(a)):
            for j in range(len(b)):
                for k in range(len(c)):
                    if abs(a[i]-b[j]) <= d and abs(a[i]-c[k]) <= d and abs(b[j]-c[k]) <= d:
                        ans += 1
        return ans
    def num_triplets(self, a, b, c, d):
        a = sorted(a)  # nlg(n)
        b = sorted(b)
        c = sorted(c)
        ans = 0
        for i in range(len(a)):
            x = a[i]
            l = bisect.bisect_left(b, x-d)
            r = bisect.bisect_right(b, x+d)

            for j in range(l, r):
                min_val = max(b[j]-d, a[i]-d)
                max_val = min(b[j]+d, a[i]+d)

                ll = bisect.bisect_left(c, min_val)
                rr = bisect.bisect_right(c, max_val)

                ans += rr-ll

        return ans



# import numpy as np
# a = np.random.randint(0, 10, (10,))
# b = np.random.randint(0, 10, (10,))
# c = np.random.randint(0, 10, (10,))

a = [9,0,3,1,3,3,9,6,9,9]
b = [4,7,4,9,1,2,2,0,5,7]
c = [4,0,3,7,8,9,5,6,0,4]

print(Solution().num_triplets_1(a, b, c, d=4))

# print(",".join(str(a).split(" ")))
# print(",".join(str(b).split(" ")))
# print(",".join(str(c).split(" ")))
