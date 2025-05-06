"""
给一个数据流，找到里面的loose median。
loose median的定义应该是 2^a <= number <= 2^(a+1)
返回区间中的一个即可 a只是为了我的表述方便如果median是5那返回[4, 8]之间任意一个都行

ChatGPT said:
明白了！你说的 loose median 是一个近似中位数，它不需要非常精确地等分数据流，而是只要满足：

该值介于某个 $2^a$ 和 $2^{a+1}$ 之间，且它能代表 median 的近似值。

✅ 举个例子来帮助理解：
数据流是：

csharp
Copy
Edit
[1, 3, 5, 6, 7, 8, 12, 13]
排序后中位数是 (6 + 7)/2 = 6.5，所以我们 loose median 应该返回 [4, 8] 之间的任何一个都行（因为 $2^2=4$, $2^3=8$）

比如：返回 5, 6, 7 都是合法的

🧠 解题目标
给定一个动态数据流（可能一个一个过来）

实时或阶段性地返回 loose median：

找出实际中位数位置

找到区间 [2^a, 2^{a+1}]，包含这个位置的值

返回区间内的任意一个即可（通常就返回实际中位数或 $2^a$）

✅ 解法 1：使用最小堆 + 最大堆（经典中位数维护）
方法思路：
最大堆保存左半边（较小的数字）

最小堆保存右半边（较大的数字）

两堆大小差距不超过 1

中位数：

如果两堆一样大 → 取两个堆顶的平均值

否则取堆更多那边的堆顶

找到中位数后，取 $\text{a} = \lfloor \log_2(\text{median}) \rfloor$，返回 $[2^a, 2^{a+1}]$ 中的任意数即可

"""


import heapq
import math

class LooseMedianFinder:
    def __init__(self):
        self.low = []  # max-heap (as negative)
        self.high = [] # min-heap

    def add(self, num):
        if not self.low or num <= -self.low[0]:
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.high, num)

        # Rebalance heaps
        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def get_loose_median(self):
        if not self.low:
            return None

        # Find real median
        if len(self.low) == len(self.high):
            median = (-self.low[0] + self.high[0]) / 2
        else:
            median = -self.low[0]

        # Find loose interval
        a = int(math.floor(math.log2(median)))
        lower = 2 ** a
        upper = 2 ** (a + 1)
        # 返回区间中的任意值，这里返回实际中位数或lower
        return int(median)  # 或 random.randint(lower, upper)
