def f(x):
    """递归排序函数"""
    # 基本情况：单个元素的序列是已经排好序的
    if len(x) <= 1:
        return x

    # 将输入序列分为奇数位置的和偶数位置的子序列
    odd_indexed = x[::2]  # 奇数索引：x1, x3, x5, ...
    even_indexed = x[1::2]  # 偶数索引：x2, x4, x6, ...

    # 递归地排序这两个子序列
    y1 = f(odd_indexed)
    y2 = f(even_indexed)

    # 合并两个排序后的子序列
    return y1+y2


# 示例使用：
n = 10
input_sequence = list(range(1, n + 1))
sorted_sequence = f(input_sequence)
print("Sorted sequence:", sorted_sequence)
