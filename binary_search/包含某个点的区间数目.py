import bisect


class IntervalQuery:
    def __init__(self, intervals):
        # 将区间的左端点和右端点分别排序
        self.intervals = sorted(intervals, key=lambda x: x[0])  # 按照左端点排序
        self.starts = [interval[0] for interval in self.intervals]  # 左端点
        self.ends = sorted([interval[1] for interval in self.intervals])  # 右端点排序

    def find_intervals(self, point):
        # 查找包含查询点的区间
        # 1. 查找所有左端点小于等于查询点的区间
        left_count = bisect.bisect_right(self.starts, point)
        # 2. 查找所有右端点小于等于查询点的区间
        right_count = bisect.bisect_left(self.ends, point)

        valid_cnt = left_count - right_count
        # 返回包含查询点的区间
        return self.intervals[right_count:left_count]


# 示例
intervals = [(1, 5), (2, 6), (3, 7), (8, 10)]
query_point = 4

interval_query = IntervalQuery(intervals)
result = interval_query.find_intervals(query_point)

print(f"Intervals containing {query_point}: {result}")
