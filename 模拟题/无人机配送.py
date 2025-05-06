"""
There are N houses (numbered from 0 to N−1) located in a straight line along a street.
The distance between houses J and K is |J−K| (an absolute difference between J and K).
A drone needs to deliver a package to each of N houses. The order in which it will visit the houses
is specified in array A. The house number K will be the A[K]-th to be visited.
For example, given A = [4, 2, 1, 3], the drone will visit the houses in the order:
* house 2 (as A[2] = 1),
* house 1 (as A[1] = 2),
* house 3 (as A[3] = 3),
* house 0 (as A[0] = 4).
What is the total distance the drone needs to travel to deliver all the packages? The drone starts at house K,
for which A[K] = 1 and ends at house L, for which A[L] = N. In the example above, the total distance the drone
will travel is equal to |2 − 1| + |1 − 3| + |3 − 0| = 6.
Write a function:
int solution(vector<int> &A);
that, given an array A, returns the total distance the drone needs to travel, starting at house K, for which A[K] = 1 and ending at house L such that A[L] = N.
Examples:
1. Given A = [4, 2, 1, 3], the function should return 6 as explained above.
2. Given A = [3, 5, 4, 2, 1], the function should return 7. The drone starts at house 4, then goes to 3, 0, 2 and 1. The total distance equals |4 − 3| + |3 − 0| + |0 − 2| + |2 − 1| = 7.
3. Given A = [1], the function should return 0. The drone does not need to change its location at all.
Assume that:
* N is an integer within the range [1..100];
* each element of array A is an integer within the range [1..N];
* the elements of A are all distinct.

这个题目描述了一个情景：有 N 个房子（从 0 到 N-1），它们沿着一条直线排成一行，距离可以通过两个房子编号的绝对差来计算。现在有一个无人机，它要根据一个给定的顺序，依次为每个房子配送包裹。任务是计算无人机总共需要行驶的距离。

题目解析：
输入： 一个数组 A，表示无人机访问房子的顺序。具体来说，A[K] 表示房子 K 会是第 A[K] 个被访问的房子。

目标： 计算无人机从第一个被访问的房子（A[K] == 1）开始，到最后一个被访问的房子（A[L] == N）结束，总共行驶的距离。

距离的计算方法：

无人机每次从一个房子飞到下一个房子，距离计算为两个房子编号的绝对差：|current_house - next_house|。

题目要求：
找到第一个被访问的房子（A[K] == 1）和最后一个被访问的房子（A[L] == N）。

计算无人机从开始房子到结束房子的总行驶距离，按照顺序依次访问所有房子。

解题思路：
首先，找到 A[K] == 1 的房子，它是无人机的起始点。

然后，找到 A[L] == N 的房子，它是无人机的终点。

计算无人机的总行驶距离：

从起点开始，按顺序访问数组 A 中的每一个房子，计算相邻两个房子之间的距离，累加即可。

特别地，如果数组的长度为 1（即只有一个房子），距离为 0。
"""