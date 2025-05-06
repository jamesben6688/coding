class Solution:
    def max_area(self, horizontal_segs, vertical_segs):
        """
        :param horizontal_segs: [[x1, x2, y]]
        :param vertical_segs: [[y1, y2, x]]
        :return:

        O(N^3)
        """
        nh = len(horizontal_segs)
        # nv = len(vertical_segs)
        max_area = -1
        for h1 in range(nh):
            for h2 in range(h1+1, nh):
                seg1 = horizontal_segs[h1]
                seg2 = horizontal_segs[h2]

                valid_verticals = []
                mx_x = -float('inf')
                mn_x = float('inf')
                for v in vertical_segs:
                    if v[0] <= seg1[2] <= v[1] and v[0] <= seg2[2] <= v[1] and \
                        seg1[0] <= v[2] <= seg1[1] and seg2[0] <= v[2] <= seg2[1]:
                        valid_verticals.append(v)
                        mx_x = max(mx_x, v[2])
                        mn_x = min(mn_x, v[2])

                max_area = max(max_area, abs(seg1[2]-seg2[2])*(mx_x-mn_x))


        return max_area


print(Solution().max_area(
    horizontal_segs=[(1, 5, 2), (1, 5, 3)],
    vertical_segs=[(-1, 3, 1), (1, 5, 5)]
))