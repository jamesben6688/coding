import bisect

def count_with_prefix(strings, prefix):
    left = bisect.bisect_left(strings, prefix)
    right = bisect.bisect_right(strings, prefix + '\uffff')
    return right - left
words = ["apple", "application", "banana", "band", "cat", "cater"]
words.sort()


print(count_with_prefix(words, "app"))  # 输出 2
print(count_with_prefix(words, "ban"))  # 输出 2
print(count_with_prefix(words, "ca"))   # 输出 2
print(count_with_prefix(words, "dog"))  # 输出 0
