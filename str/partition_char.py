def get_valid_ch(s, k):
    i = 0
    prev=None
    cur=None
    prev_p = None
    ans = []
    while i < len(s):
        cur = s[i]
        print(prev, cur)
        if prev and cur != prev:
            if prev != prev_p:
                ans.append(prev)

        if i % k == 0:
            prev_p = prev
        i += 1
        prev = cur

    if cur != prev_p:
        ans.append(cur)
    return ans


print(get_valid_ch("AABBCCDDEFG", 3))

"""
AAB BCC DDE FG
"""