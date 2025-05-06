"""
给一个2D matrix，每个元素都是int。可以从矩阵任何一个元素出发进行游走，游走规则：
（1）可以去所在row中strictly比它大的元素
（2）可以去所在col中strictly比它大的元素
如果没有符合游走规则的选项，视为path终止；path中遍历到的所有元素的int的和，视为pathSum
要求从所有path中选择pathSum最大的path，将其pathSum返回
【follow up】
不单单是返回pathSum，同时也要返回path是什么

https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/description/
329 矩阵中的最长递增路径

"""