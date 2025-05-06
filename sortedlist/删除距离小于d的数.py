"""
浮点型的data stream存到内存中，当检测到有三个数字两两之间“distance”小于“d”，则返回这三个数字，并且把这三个数从内存中删除

Given a data stream and a distance d, output three values that within distance d, if less than three values, return None
For example:
d = 10
input 1 -> None
input 2 -> None
input 20 -> None
input 50 -> None
input 5 ->  [1, 2, 5]
input 4 -> None
"""