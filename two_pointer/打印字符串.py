"""
abc 2输出 abcabc
abc2 de3 输出 abcabcdeabcabcdeabcabcde
"""
# class Solution:
#     def print_str(self, s):


def decode_and_print(s: str):
    i = 0
    output_len = 0

    while i < len(s):
        if s[i].isdigit():
            # 解析多位数字
            repeat = 0
            while i < len(s) and s[i].isdigit():
                repeat = repeat * 10 + int(s[i])
                i += 1

            for j in range(repeat):
                decode_and_print(s[:-1])

        else:
            print(s[i], end="")
        i += 1

# 示例运行
decode_and_print("abc3de2")

"""
abcabcabcdeabcabcde
"""





decode_and_print("abc2 de3")

