"""
最大的10个files in a filesystem. 标准的heap题目，用了两种解法遍历 filesystem，讨论了各种复杂度，performance。

最大的10个files in a filesystem. 标准的heap题目，用了两种解法遍历 filesystem，讨论了各种复杂度，performance。

这是一个典型的使用 Heap 求 Top-K 的题目场景，面试里经常出现，比如「找文件系统中最大的 10 个文件」。下面我会用面试常见的方式来总结和分析这个题目：

📌 题目定义：
给定一个文件系统，找出最大的 10 个文件（按文件大小）

你可以假设文件系统是一个类似如下的树结构：


"""
class FileNode:
    def __init__(self, name, size=0, is_file=False, children=None):
        self.name = name
        self.size = size  # size only valid when is_file == True
        self.is_file = is_file
        self.children = children or []  # type: List[FileNode]


"""
解题思路：Top-K + Tree Traversal
我们要遍历整棵文件树，然后找出最大的 10 个文件：

✅ 两种核心方法：
方法一：使用最小堆（Min Heap）维护 Top-10
思路：

用一个大小为 10 的最小堆（heapq）

遍历整个文件树

每遇到一个文件，就尝试加入堆中

如果堆大小 < 10，直接加

否则，如果新文件比堆顶更大，则弹出堆顶再加入

优点：

内存稳定，空间复杂度 $O(10) = O(1)$

性能好，适用于大规模文件系统

Python 简版伪代码：
"""
import heapq

def find_largest_files(root):
    heap = []

    def dfs(node):
        if node.is_file:
            if len(heap) < 10:
                heapq.heappush(heap, (node.size, node.name))
            else:
                if node.size > heap[0][0]:
                    heapq.heappushpop(heap, (node.size, node.name))
        else:
            for child in node.children:
                dfs(child)

    dfs(root)
    return sorted(heap, reverse=True)


"""
方法二：用数组收集后排序
思路：

遍历整个文件系统，把所有文件和大小收集进数组

排序后取最大的前 10 个

优点：

实现简单

适用于文件数量不多的情况

缺点：

空间复杂度 $O(N)$，当文件非常多时会内存爆炸

不适合大规模数据
"""
def find_largest_files_simple(root):
    all_files = []

    def dfs(node):
        if node.is_file:
            all_files.append((node.size, node.name))
        else:
            for child in node.children:
                dfs(child)

    dfs(root)
    return sorted(all_files, reverse=True)[:10]


"""
多线程扫描文件系统（并行 DFS）

懒加载文件大小（只对需要的文件调用系统 API）

I/O 读取优化（比如使用异步 I/O）

处理符号链接 / 循环引用

早停机制（如果你只想要超过一定大小的文件）

🧪 面试官可能进一步问：
如果文件系统太大，无法全部加载内存怎么办？

答：流式处理 + min heap（方法一）

如果文件是分布式的？

答：每个子系统做 top-10，最后 merge top-10s

如果是 top-10 最大文件夹（含子目录文件大小总和）？

答：DFS 返回子文件大小总和 + max heap 记录文件夹名和其大小
"""