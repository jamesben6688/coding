"""
size 指向栈顶元素, i指向入栈的数字, j指向出栈的数字
"""

def validateStackSequences(pushed, popped):
    size = 0
    j = 0
    for i in range(len(pushed)):
        pushed[size] = pushed[i]
        size += 1
        while size != 0 and pushed[size - 1] == popped[j]:
            size -= 1
            j += 1
    return size == 0

print(validateStackSequences([x for x in range(1, 6)], [2, 5, 4, 3, 1]))  # False)
