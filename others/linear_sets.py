"""
问题描述
给定一组 线性区间（线性集），每个区间 [L, R] 包含从 L 到 R 的所有整数，我们的目标是找到一个最小的集合，
包含该集合与每个线性集的交集（即有至少一个元素与每个区间重合）。

解决思路
这个问题可以通过 贪心算法 来解决。我们通过以下步骤来构建解决方案：

排序区间： 首先，我们将所有区间按它们的右端点（R）进行排序。排序的目的是确保我们可以尽量早地选定一个能够与尽可能多的区间发生交集的点。

贪心选择点： 然后，遍历排序后的区间，依次选择点：

对于每一个区间 [L, R]，我们要确保至少有一个点与它发生交集。

如果当前的集合中没有任何一个点与区间 [L, R] 有交集，那么我们就选择区间的右端点 R 作为一个新点，因为这个点能够与当前区间产生交集，
并且它可能还会与后面的区间产生交集。

终止条件： 当我们遍历完所有区间后，得到的点集合就是最小的点集合，能够与所有区间产生交集。

"""
def min_intersection_points(sets):
    # Step 1: Sort the intervals by their right endpoint (R)
    sets.sort(key=lambda x: x[1])

    # Step 2: Initialize a list to store the result points
    points = []

    # Step 3: Process each interval in the sorted list
    for interval in sets:
        # If the last point does not intersect the current interval
        if not points or points[-1] < interval[0]:
            # Add the right endpoint of the current interval to the points list
            points.append(interval[1])

    # Return the number of points that form the minimal set of intersections
    return points


# Example usage:
# sets = [[1, 3], [2, 5], [4, 8], [7, 10]]
# sets = [[1,2],[2,3],[3,4],[4,5]]
# sets = [[10,16],[2,8],[1,6],[7,12]]
sets = [[1, 7], [2, 6], [8, 9]]
result = min_intersection_points(sets)
print(result)  # Output the points of the minimum intersection set