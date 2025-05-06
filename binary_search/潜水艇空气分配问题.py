"""

if you have an array of submarine A,
and K person, try to find a way to accomodate people into submarines make the the person who
have the least unit of air maxmium
for example,
A = [10, 6, 4, 3, 2], k = 4
P = [2, 1, 1, 0, 0]
第一个潜水艇每人占5unit， 第二个潜水艇每人占6unit，第三个占4unit，
这样最少人占4个unit空气。

解法：二分答案 + 贪心验证
二分搜索答案：

最小空气单位的下限是 0

上限是最大潜水艇空气量（比如 max(A)）

通过二分找出最大的可能空气单位 x，满足可以把 k 个人合理分配。

贪心验证函数：

给定一个最小空气单位 x，我们检查是否可以用当前的潜水艇分配出不少于 k 个“人份”。

对于每个潜水艇 a，它最多可以安排 floor(a / x) 个这样分到不少于 x 单位空气的人。

"""

def max_min_air(A, k):
    def can_allocate(min_air):
        # 计算在 min_air 的情况下，最多能分给多少人
        return sum(a // min_air for a in A) >= k

    left, right = 1, max(A)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if can_allocate(mid):
            answer = mid  # 这个 min_air 是可行的，尝试更大的
            left = mid + 1
        else:
            right = mid - 1

    return answer


A = [10, 6, 4, 3, 2]

k = 4
print(max_min_air(A, k))  # 输出: 4


