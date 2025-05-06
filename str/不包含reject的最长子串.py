def longest_substring_without_reject(target: str, reject: str) -> str:
    reject_set = set(reject)
    max_len = 0
    max_substr = ""
    start = 0

    for end in range(len(target)):
        if target[end] in reject_set:
            # 当前字符非法，更新起点
            start = end + 1
        else:
            # 当前子串合法，判断是否更新最长
            curr_len = end - start + 1
            if curr_len > max_len:
                max_len = curr_len
                max_substr = target[start:end + 1]

    return max_substr


print(longest_substring_without_reject("abcxdeyzfgh", "dx"))  # 输出: "yzfgh"
print(longest_substring_without_reject("apple", "p"))         # 输出: "le"
print(longest_substring_without_reject("abcdef", "xyz"))      # 输出: "abcdef"
