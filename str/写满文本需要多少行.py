def wrap_dp(s1, s2, max_width):
    """
        动态规划

        状态定义：
            设 dp[i][j] 表示从 s1[i:] 和 s2[j:] 开始排版，所需的最小行数。

            i 是当前还没处理的 s1 中的单词位置

            j 是当前还没处理的 s2 中的单词位置

            状态转移：
            枚举从 s1[i:] 选多少个单词 i1，从 s2[j:] 选多少个单词 j1，只要拼在一起的总长度（加空格） ≤ max_width，我们就可以写成一行：

            dp[i][j] = min(dp[i][j], 1 + dp[i+i1][j+j1])

            边界：
                当 i == len(s1) 且 j == len(s2)，表示都排完了，返回 0 行。

    :param s1:
    :param s2:
    :param max_width:
    :return:
    """
    s1_words = s1.split()
    s2_words = s2.split()
    m, n = len(s1_words), len(s2_words)

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(i, j):
        if i == m and j == n:
            return 0, []

        min_lines = float('inf')
        best_choice = None

        for i1 in range(1, m - i + 1):
            left_chunk = s1_words[i:i+i1]
            left_len = sum(len(w) for w in left_chunk) + (i1 - 1)
            if left_len >= max_width:
                break

            for j1 in range(1, n - j + 1):
                right_chunk = s2_words[j:j+j1]
                right_len = sum(len(w) for w in right_chunk) + (j1 - 1)
                total_len = left_len + 1 + right_len
                if total_len <= max_width:
                    next_lines, next_path = dp(i + i1, j + j1)
                    if 1 + next_lines < min_lines:
                        min_lines = 1 + next_lines
                        best_choice = [(left_chunk, right_chunk)] + next_path
                else:
                    break

        return min_lines, best_choice if best_choice is not None else []

    total_lines, path = dp(0, 0)

    # format the output
    output_lines = []
    for left_words, right_words in path:
        left_text = " ".join(left_words)
        right_text = " ".join(right_words)
        space = max_width - len(left_text) - len(right_text)
        output_lines.append(left_text + " " * space + right_text)

    return total_lines, output_lines

"""
hello openAI
world builds inteelligent tools
this is left size on the right
"""

print(wrap_dp(s1 = "hello world this is left side",
s2 = "OpenAI builds intelligent tools on the right",
max_width = 30))





