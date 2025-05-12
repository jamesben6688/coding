def count_valid_password_substrings(s):
    total = 0
    n = len(s)

    for length in range(6, 11):  # 长度从6到10
        for i in range(n - length + 1):
            substr = s[i:i+length]
            letters = sum(c.isalpha() for c in substr)
            digits = sum(c.isdigit() for c in substr)
            if letters >= 2 and digits >= 2:
                total += 1

    return total
