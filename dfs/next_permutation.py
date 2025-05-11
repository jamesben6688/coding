"""我们把问题分为两部分：

A. 处理数字和小数点：
拆出小数点的位置和数字部分；

保存为：digits = ['4', '3', '2', '1']，dot_pos = 3（比如在 '432.1'）

B. 进行下一个排列：
尝试对 digits 做 next_permutation；

如果已经是最大排列：

将 digits 排成升序；

移动 dot（小数点）：

如果不在末尾：dot_pos += 1;

如果在末尾：dot_pos = 0（移到最左边）
"""

def next_permutation_with_dot(s):
    # Step 1: Extract digits and dot position
    dot_pos = s.index('.')
    digits = list(s.replace('.', ''))

    # Step 2: Try next permutation
    if not next_permutation(digits):
        # Already at max permutation — reset to smallest and move dot
        digits.sort()
        if dot_pos < len(digits):  # dot not at end
            dot_pos += 1
        else:  # dot at end → move to front
            dot_pos = 0

    # Step 3: Reconstruct with new dot
    digits_with_dot = digits[:dot_pos] + ['.'] + digits[dot_pos:]
    return ''.join(digits_with_dot)


# Standard next_permutation for list of chars
def next_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        return False  # no next perm

    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    return True

print(next_permutation_with_dot("432.1"))  # → 1234.
print(next_permutation_with_dot("4321."))  # → .1234
print(next_permutation_with_dot(".1234"))  # → .1243
print(next_permutation_with_dot("12.34"))  # → 12.43