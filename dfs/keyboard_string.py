"""
字符位置的预处理：我们只需要遍历键盘的每个字符，将它们的坐标保存到字典中。这是 O(m * n) 的操作，其中 m 是键盘的行数，n 是列数。

跳跃判断：对于每对相邻的字符，判断它们之间的曼哈顿距离是 O(1) 的操作。因此，对单词的遍历长度为 L，总时间复杂度是 O(L)。

总的时间复杂度：因此，整个过程的时间复杂度是 O(m * n + L)，其中 L 是单词的长度。

空间复杂度：
字符位置字典：存储每个字符的坐标，需要 O(m * n) 空间。

常数空间：除了字典外，其他的数据结构占用的空间是常数的。

因此，空间复杂度是 O(m * n)。

O(m * n + L)
"""

def can_type_word(keyboard, k, word):
    # 获取键盘的行列数
    m = len(keyboard)
    n = len(keyboard[0])

    # 找到所有字符的位置
    key_positions = {}
    for i in range(m):
        for j in range(n):
            key_positions[keyboard[i][j]] = (i, j)

    # 计算曼哈顿距离
    def manhattan_distance(c1, c2):
        x1, y1 = key_positions[c1]
        x2, y2 = key_positions[c2]
        return abs(x1 - x2) + abs(y1 - y2)

    # 遍历word中的每一对相邻字符，检查曼哈顿距离
    for i in range(len(word) - 1):
        current_char = word[i]
        next_char = word[i + 1]

        # 计算当前字符和下一个字符的曼哈顿距离
        if manhattan_distance(current_char, next_char) > k:
            return False  # 如果距离太大，不能输入该单词

    return True  # 如果所有字符都能顺利输入，返回True


"""
followup: 可以重复
"""
from collections import defaultdict


def can_type_word(keyboard, k, word):
    m, n = len(keyboard), len(keyboard[0])

    # Step 1: 构建每个字符的所有可能位置
    char_positions = defaultdict(list)
    for i in range(m):
        for j in range(n):
            char_positions[keyboard[i][j]].append((i, j))

    # Step 2: 初始化起点（第一个字符的所有位置）
    if word[0] not in char_positions:
        return False
    current_positions = char_positions[word[0]]

    # Step 3: 对于每个字符，从上一次可达的位置出发，找出下一个可达的位置
    for idx in range(1, len(word)):
        target_char = word[idx]
        if target_char not in char_positions:
            return False

        next_positions = []
        for (x1, y1) in current_positions:
            for (x2, y2) in char_positions[target_char]:
                if abs(x1 - x2) + abs(y1 - y2) <= k:
                    next_positions.append((x2, y2))

        if not next_positions:
            return False  # 没有任何合法的跳跃路径

        current_positions = next_positions  # 进入下一轮

    return True


# dfs: 用三维数组存visited
# memo: (LMN), L为字符串长度。总的状态数LMN
def can_type_word_dfs(keyboard, k, word):
    from collections import defaultdict

    m, n = len(keyboard), len(keyboard[0])
    pos = defaultdict(list)
    for i in range(m):
        for j in range(n):
            pos[keyboard[i][j]].append((i, j))

    visited = set()

    def dfs(index, x, y):
        if index == len(word):
            return True

        key = (index, x, y)
        if key in visited:
            return False
        visited.add(key)

        for nx, ny in pos[word[index]]:
            if abs(nx - x) + abs(ny - y) <= k:
                if dfs(index + 1, nx, ny):
                    return True
        return False

    # 从首字母的所有位置出发
    for x, y in pos[word[0]]:
        if dfs(1, x, y):
            return True
    return False
