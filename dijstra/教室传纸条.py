"""
说一个教室里的学生传纸条，从第一排开始 横向传，被抓住的几率是 90%，纵向传被抓住的几率是50%，每往后一排被抓住的几率要减少一半，
横向纵向都减少。最后要计算的是从学生A 到B，被抓的最小几率是多少。

这个题目是一个 有权重的图最短路径问题（或者概率传播问题），其中：

每个学生在一个二维 grid 中，比如 grid[i][j] 表示第 i 排第 j 个学生。

横向传（左右邻居）起始概率是 90% 会被抓（=10% 成功传递），

纵向传（上下邻居）起始概率是 50% 会被抓（=50% 成功传递），

每往后一排，抓的几率减半，也就是成功的概率增加，用于更新传递路径。

✅ 模型建构思路
可以把每个学生当成一个图中的节点，传纸条就是从一个节点到邻居节点传递信息的操作，有成功概率。

边的权重：可以设为 “被抓的概率” 或 “成功概率”。

最终我们要找一条从 A 到 B 的路径，使得总成功概率最大，或者总失败概率最小。

✅ 转换方式：从“概率乘积”到“路径最短”
在图中找一条路径，路径上的每条边都有一个“成功概率”，总成功概率就是这些边的乘积：

text
Copy
Edit
P = p1 * p2 * p3 * ...
我们无法直接在图上用 Dijkstra 求乘积最大路径，但我们可以：

取 -log(success_prob) 作为边权重！
因为：

text
Copy
Edit
maximize(p1 * p2 * ...) <=> minimize(-log(p1) + -log(p2) + ...)
所以我们可以把图转化成最短路径问题，然后用 Dijkstra 算法来解。

✅ 实现步骤
建图：

横向邻居：success_prob = 1 - 0.9 * decay_factor[i]

纵向邻居：success_prob = 1 - 0.5 * decay_factor[i]

decay_factor[i] = 0.5 ** i

边权：

每条边的权重 = -log(success_prob)

用 Dijkstra 从 A 到 B，记录最小路径和

返回被抓概率 = 1 - e^{-sum of weights}
"""