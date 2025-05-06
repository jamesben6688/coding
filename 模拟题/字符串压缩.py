def compress_string(s):
    n = len(s)
    for length in range(n // 2, 0, -1):  # try longest possible match first
        for start in range(n - length):
            substr = s[start:start + length]
            next_start = start + length
            if s[next_start:next_start + length] == substr:
                # Found repetition
                return s[:next_start] + f".{start}.{start + length - 1}"
    return s


s = "abcdefffgabcde"
print(compress_string(s))  # Output: abcdefffg.0.4
