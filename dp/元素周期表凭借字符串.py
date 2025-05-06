"""

判断它能否用元素周期表里的元素表示，如PrAcTiCe。Ignore cases。return true or false.
由于元素符号只能是一位或两位字母，可以DP。递推式:
DP(i) = (DP(i - 1) and word in chemElements) or (DP(i - 2) and word[i - 1: i + 1] in chemElements)
"""

def can_be_formed_by_elements_dp(s):
    element_symbols = {
        'h', 'he', 'li', 'be', 'b', 'c', 'n', 'o', 'f', 'ne',
        'na', 'mg', 'al', 'si', 'p', 's', 'cl', 'ar',
        'k', 'ca', 'sc', 'ti', 'v', 'cr', 'mn', 'fe', 'co', 'ni',
        'cu', 'zn', 'ga', 'ge', 'as', 'se', 'br', 'kr',
        'rb', 'sr', 'y', 'zr', 'nb', 'mo', 'tc', 'ru', 'rh', 'pd',
        'ag', 'cd', 'in', 'sn', 'sb', 'te', 'i', 'xe',
        'cs', 'ba', 'la', 'ce', 'pr', 'nd', 'pm', 'sm', 'eu', 'gd',
        'tb', 'dy', 'ho', 'er', 'tm', 'yb', 'lu',
        'hf', 'ta', 'w', 're', 'os', 'ir', 'pt', 'au', 'hg',
        'tl', 'pb', 'bi', 'po', 'at', 'rn',
        'fr', 'ra', 'ac', 'th', 'pa', 'u', 'np', 'pu', 'am', 'cm',
        'bk', 'cf', 'es', 'fm', 'md', 'no', 'lr',
        'rf', 'db', 'sg', 'bh', 'hs', 'mt', 'ds', 'rg', 'cn', 'uut',
        'fl', 'uup', 'lv', 'uus', 'uuo'
    }

    s = s.lower()
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # 空字符串合法

    for i in range(1, n + 1):
        if i >= 1 and dp[i - 1] and s[i - 1:i] in element_symbols:
            dp[i] = True
        if i >= 2 and dp[i - 2] and s[i - 2:i] in element_symbols:
            dp[i] = True

    return dp[n]
