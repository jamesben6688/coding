"""
O(Nlg(N))
"""

import mpmath


n = 1000
# 设置需要计算的精度，这里设置为 n 位
mpmath.mp.dps = n  # 设置小数点后面多少位

# 获取 pi 的字符串表示，包括整数部分 "3" 和小数部分
pi_str = str(mpmath.mp.pi)[2:]  # 获取小数部分，去掉 "3."

# 将整数部分 "3" 加入到字符串的最前面，作为 index 1 的部分
pi_str = '3' + pi_str  # 将整数部分 "3" 加到字符串的最前面

for i in range(1000):
    # print(pi_str[i-len(str(i)):i+1])
    if int(pi_str[i-len(str(i))+1:i+1]) == i+1:
        print(i)
        break