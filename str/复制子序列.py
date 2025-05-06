def min_copies_to_form_subsequence(source, target):
    from collections import defaultdict

    # 先构建 source 中所有字符的位置索引（加速匹配）
    source_set = set(source)
    for ch in target:
        if ch not in source_set:
            return -1  # target 中有字符 source 不含，无法匹配

    copies = 0
    i = 0  # pointer in source
    j = 0  # pointer in target

    while j < len(target):
        i = 0
        start_j = j  # 记录当前 target 位置

        while i < len(source) and j < len(target):
            if source[i] == target[j]:
                j += 1
            i += 1

        if start_j == j:
            # 本轮一次字符都没匹配，说明 source 不含 target[j]
            return -1
        copies += 1

    return copies



class Solution:
    def get_min(self, a, b):
        ans = 0
        s = ""
        i = 0
        j = 0
        prev_i = 0
        while True:
            s += a
            while i < len(b) and j < len(s):
                if b[i] == s[j]:
                    i += 1

                j += 1

            if i == len(b):
                return True, ans

            if i == prev_i:
                return False, -1

            prev_i = i
            ans += 1

print(Solution().get_min(a = "abc", b = "abcbac"))

