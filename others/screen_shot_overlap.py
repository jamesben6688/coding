def longest_overlap(img1, img2):
    base = 911
    mod = 10 ** 9 + 7
    n = len(img1)
    m = len(img2)

    # Rolling hash from the end of img1
    max_len = min(n, m)
    pow_base = [1] * (max_len + 1)
    for i in range(1, max_len + 1):
        pow_base[i] = (pow_base[i - 1] * base) % mod

    hash1 = 0  # suffix of img1
    hash2 = 0  # prefix of img2
    res = 0

    for l in range(1, max_len + 1):
        # A 的后缀哈希
        hash1 = (img1[-l] * pow_base[0] + hash1) % mod
        # B 的前缀哈希
        hash2 = (hash2 * base + img2[l - 1]) % mod

        if hash1 == hash2:
            res = l  # update longest match

    return res
