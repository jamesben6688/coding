"""
第一轮是minimumstepsofswappingstring：inputstring:dcbaexpectstring:abcdoutput：howmanyswapneeded
要求一次只能挑一个char只能和左右相邻的char换位置我给的解法用BFS类似wordladder
当时面试官引导的解法是:从头遍历inputstring然后计算步数
以上面为例dcba->abcd1dcba
将a换到index=0需要3步->adcb
将b换到index=1需要2步->abcd一共需要5步


实际上，这个问题可以优化成更快的解法 —— 目标是让每个字符在目标位置出现，靠冒泡交换它们过去。

比如从 dcba 变到 abcd，可以看成逐个把 a、b、c、d 通过交换推到它们在目标字符串的位置上。
"""