from collections import defaultdict

def parse(s):
    def helper(index):
        count_map = defaultdict(int)
        while index < len(s):
            char = s[index]
            if char == ')':
                return count_map, index
            elif char == '(':
                sub_map, next_index = helper(index + 1)
                index = next_index + 1
                # 获取括号后的数字
                repeat = 0
                while index < len(s) and s[index].isdigit():
                    repeat = repeat * 10 + int(s[index])
                    index += 1
                repeat = repeat or 1
                for k in sub_map:
                    count_map[k] += sub_map[k] * repeat
            elif char.isalpha():
                letter = char
                index += 1
                num = 0
                while index < len(s) and s[index].isdigit():
                    num = num * 10 + int(s[index])
                    index += 1
                num = num or 1
                count_map[letter] += num
            else:
                index += 1  # 安全跳过未知字符
        return count_map, index

    result, _ = helper(0)
    return result


print(parse("A3B2"))           # {'A': 3, 'B': 2}
print(parse("(A3B2)2"))        # {'A': 6, 'B': 4}
print(parse("A2(A3B2)2"))      # {'A': 8, 'B': 4}
print(parse("A2(B3(C2)2)2"))   # {'A': 2, 'B': 6, 'C': 12}
