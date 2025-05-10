"""
一个奇怪的sorting算法 要挂就是这一轮 sorting需要swap数字 要求是数字不能向左移动超过2位，求最优的sorting结果

问题定义：
给定一个数组 arr，它不是完全乱序的，而是每个元素在原数组中的位置最多只和它在排序后的位置相差 k，也就是说：

对于任意元素 arr[i]，它在最终排序后的位置是 j，则 |i - j| < k

其中 k 是一个很小的数，k << len(arr)。

✅ 最优解法：最小堆（Min Heap）
由于每个元素最多只会“错位”到前后 k 个位置，所以可以用 大小为 k 的最小堆 来维护局部有序性。

🔧 算法步骤（时间复杂度 O(n log k)）：
初始化一个最小堆（大小最多为 k）

将前 k 个元素加入堆中

从堆中弹出最小元素（最早可能正确排序的位置），并将下一个新元素入堆

重复直到处理完所有元素

最后清空堆中剩余的元素

时间和空间复杂度：
操作	复杂度
时间复杂度	O(n log k)
空间复杂度	O(k)

"""

import heapq

def sort_k_sorted_array(arr, k):
    n = len(arr)
    result = []
    min_heap = []

    # Step 1: Push first k elements to heap
    for i in range(min(k + 1, n)):
        heapq.heappush(min_heap, arr[i])

    # Step 2: Process remaining elements
    for i in range(k + 1, n):
        result.append(heapq.heappop(min_heap))
        heapq.heappush(min_heap, arr[i])

    # Step 3: Extract remaining elements
    while min_heap:
        result.append(heapq.heappop(min_heap))

    return result


arr = [3, 1, 4, 2, 5, 7, 6]
k = 2
print(sort_k_sorted_array(arr, k))  # 输出：[1, 2, 3, 4, 5, 6, 7]
