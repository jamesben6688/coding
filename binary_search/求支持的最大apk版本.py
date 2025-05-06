"""
1. ApkVersions是一个三元组的list，ApkVersions[i] = (ApkVer, minOSVersion, maxOSVersion)，
描述了当前的Apk Version, 以及它支持的OS的最低和最高version
2. OSVersions是一个单纯的数组，OSVersions[j] 描述一个OS version
输出是为每一个OSVersions中的元素OSVersions[j]，找到最新(最大)的ApkVer满足 minOSVerion <= OSVersion[i] <= maxOSversion.
Solution是，先过一遍ApkVersions，合并可以合并的range，保持这个range中最大的ApkVer，然后按照range排序。
接着为每一个OSversions[j], 用binary search找到满足条件的range，取出对应的ApkVer.
其实solution不难，刚放下电话就想到了……就是面试过程中想不到，还是经验太少了……紧张了……😮‍💨

先将range按照起始点排序, 找MinOS <= os的left, maxOs >= os的right

然后求max(apk[left:right+1])

解法:
我们把每个区间 (minOS, maxOS) 转成两个事件：

(minOS, apkVer, "add")：表示从这里开始支持 apkVer

(maxOS + 1, apkVer, "remove")：表示从这里结束支持 apkVer

然后把所有事件按位置排序，从左到右扫描，用一个堆（或 multiset）维护当前活跃的 ApkVer 集合，取最大值。

 时间复杂度分析
预处理：O(n log n)（排序 + 堆操作）；

查询：O(m log k)，k 是分段个数；

空间复杂度：O(n)。

如果你有百万级数据，这个版本是推荐选项。需要我进一步做成模块封装，或者加缓存支持、动态更新吗？
"""
from collections import defaultdict
import bisect
import heapq

def preprocess_by_scanline(ApkVersions):
    events = []
    for apkVer, minOS, maxOS in ApkVersions:
        events.append((minOS, apkVer, "add"))
        events.append((maxOS + 1, apkVer, "remove"))

    # 排序：位置升序；add 操作在 remove 之前
    events.sort(key=lambda x: (x[0], 0 if x[2] == "add" else 1))

    active = defaultdict(int)  # 记录每个 apkVer 出现次数
    heap = []  # max-heap（用负值）
    intervals = []

    prev_pos = None

    for pos, apkVer, typ in events:
        if prev_pos is not None and prev_pos < pos:
            # 有活跃的 apkVer，才记录区间
            while heap and active[-heap[0]] == 0:
                heapq.heappop(heap)
            if heap:
                max_apk = -heap[0]
                intervals.append((prev_pos, pos, max_apk))

        if typ == "add":
            active[apkVer] += 1
            heapq.heappush(heap, -apkVer)
        else:
            active[apkVer] -= 1

        prev_pos = pos

    return intervals


def find_apk_for_os(intervals, OSVersions):
    starts = [s for s, e, v in intervals]
    result = []
    for osv in OSVersions:
        idx = bisect.bisect_right(starts, osv) - 1
        if idx >= 0:
            s, e, v = intervals[idx]
            if s <= osv < e:
                result.append(v)
                continue
        result.append(None)
    return result

#
# Intervals:
# (1, 4, 2)
# (4, 5, 3)
# (5, 8, 5)
# (8, 10, 5)
# (10, 11, 5)
# (11, 12, 6)
# (12, 16, 6)
#
# Query Result:
# [2, 3, 5, 5, 6, 6, None]
