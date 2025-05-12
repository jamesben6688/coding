from collections import Counter

def can_form_palindrome(words):
    count = Counter(words)
    center_used = False

    for word in list(count.keys()):
        rev = word[::-1]
        if word == rev:
            # 是回文串，需要数量是偶数，最多允许一个奇数个
            if count[word] % 2 == 1:
                if center_used:
                    return False  # 已经有一个回文串当中心了
                center_used = True
        else:
            if count[word] != count[rev]:
                return False
            # 清除互补对，防止重复判断
            count[rev] = 0

    return True



print(can_form_palindrome(['aab', 'aba', 'baa']))