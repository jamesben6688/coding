class SegmentTree:
    def __init__(self, arr):
        arr = [0] + arr
        n = len(arr)
        # 统计和
        self.sum = [0] * (4*n)

        # 统计连续0的最长子串长度
        self.len0 = [0] * (4*n)

        # 连续0的最长前缀长度
        self.pre0 = [0] * (4*n)

        # 连续0的最长后缀长度
        self.suf0 = [0] * (4*n)

        # 连续1的最长子串长度
        self.len1 = [0] * (4*n)

        # 连续1的最长前缀长度
        self.pre1 = [0] * (4*n)

        # 连续1的最长后缀长度
        self.suf1 = [0] * (4*n)

        self.arr = arr
        self.build(1, n-1, 1)
        self.n = n

    def build(self, l, r, i):
        """
            O(Nlg(N))
        :param l:
        :param r:
        :param i:
        :return:
        """
        if l == r:
            self.sum[i] = self.arr[l]
            if self.arr[l] == 0:
                self.len0[i] = self.pre0[i] = self.suf0[i] = 1
                self.len1[i] = self.pre1[i] = self.suf1[i] = 0
            else:
                self.len0[i] = self.pre0[i] = self.suf0[i] = 0
                self.len1[i] = self.pre1[i] = self.suf1[i] = 1
            # self.len0[i] = self.pre0[i] = self.suf0[i] = self.arr[l] == 0 ? 1: 0;
            # self.len1[i] = self.pre1[i] = self.suf1[i] = self.arr[l] == 1 ? 1: 0;
        else:
            mid = (l + r) >> 1
            self.build(l, mid, i << 1)
            self.build(mid + 1, r, (i << 1) | 1)
            self.up(i, l_len=mid-l+1, r_len=r-mid)

    def up(self, i, l_len, r_len):
        # self.sum[i] = self.sum[i << 1] + self.sum[(i << 1) | 1]

        l = i << 1
        r = i << 1 | 1

        self.sum[i] = self.sum[l] + self.sum[r]
        self.len0[i] = max(self.len0[l], self.len0[r], self.suf0[l] + self.pre0[r])
        self.pre0[i] = self.pre0[l] if self.len0[l] < l_len else (self.pre0[l] + self.pre0[r])
        self.suf0[i] = self.suf0[r] if self.len0[r] < r_len else (self.suf0[l] + self.suf0[r])
        self.len1[i] = max(self.len1[l], self.len1[r], self.suf1[l] + self.pre1[r])
        self.pre1[i] = self.pre1[l] if self.len1[l] < l_len else (self.pre1[l] + self.pre1[r])
        self.suf1[i] = self.suf1[r] if self.len1[r] < r_len else (self.suf1[l] + self.suf1[r])

    def query(self, jobl, jobr):
        """
            lg(N)
        :param jobl:
        :param jobr:
        :return:
        """
        def get_res(jobl, jobr, l, r, i):
            if jobl <= l and r <= jobr:
                return self.sum[i]

            mid = (l + r) >> 1
            # down(i, mid - l + 1, r - mid)

            ans = 0
            if jobl <= mid:
                ans += get_res(jobl, jobr, l, mid, i << 1)

            if jobr > mid:
                ans += get_res(jobl, jobr, mid + 1, r, (i << 1) | 1)

            return ans
        return get_res(jobl+1, jobr+1, 1, self.n-1, 1)

    def query_longest_1(self, jobl, jobr):
        def query_longest(jobl, jobr, l, r, i):
            if jobl <= l and r <= jobr:
                return [self.len1[i], self.pre1[i], self.suf1[i]]
            else:
                mid = (l + r) // 2
                ln = mid - l + 1
                rn = r - mid
                # down(i, ln, rn)

                if jobr <= mid:
                    return query_longest(jobl, jobr, l, mid, i << 1)
                if jobl > mid:
                    return query_longest(jobl, jobr, mid + 1, r, i << 1 | 1)

                l3 = query_longest(jobl, jobr, l, mid, i << 1)
                r3 = query_longest(jobl, jobr, mid + 1, r, i << 1 | 1)

                llen, lpre, lsuf = l3
                rlen, rpre, rsuf = r3

                total_len = max(llen, rlen, lsuf + rpre)

                # pre boundary
                left_impact = mid - max(jobl, l) + 1
                if llen < left_impact:
                    total_pre = lpre
                else:
                    total_pre = lpre + rpre

                # suf boundary
                right_impact = min(r, jobr) - mid
                if rlen < right_impact:
                    total_suf = rsuf
                else:
                    total_suf = lsuf + rsuf

                return [total_len, total_pre, total_suf]

        return query_longest(jobl + 1, jobr + 1, 1, self.n - 1, 1)


arr = [2, 3, 4, 5, 6, 1]
seg_tree = SegmentTree(arr)
# print(seg_tree.tree_arr)
print(seg_tree.query(1, 3))
