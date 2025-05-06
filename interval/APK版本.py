"""
题目：不同android apk 有最低支持SDK版本，最高支持SDK版本
   Min SDK version    Max SDK version
APK 1:   4            -
APK 2:   7            10
APK 3:   -            16
APK .....
(- 代表没有上下限）
Input: (4, max), (7, 10), (min, 16)           -> 所有APK所支持版本的区间
Output: (min, 3], (3, 7), [7, 11), [11, 17), [17, max)  -> 所有SDK 区间，要求相邻区间被支持的APK 不能完全一样
Clarification:
(min, 3) -> APK 3   // 问：为什么第一个区间不能用(min, 4] 。 答：(min, 4] 和 相邻的 (4, 7) 被支持的APK 完全一样
[3, 7) -> APK 1, 3 // 问: (min, 3) 和 [3, 7) 能合并吗。 答：不能
[7, 11)  -> APK 1, 2, 3
[11, 17) -> APK 1, 3
[17, max) -> APK 1

"""