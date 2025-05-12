def can_win(tiles):
    # 使用 memoization 来缓存状态，避免重复计算
    memo = {}

    def dfs(tiles):
        # 如果当前状态已经计算过，直接返回结果
        if tuple(tiles) in memo:
            return memo[tuple(tiles)]

        # 如果所有瓷砖已经没有剩余了，表示当前玩家输了（没有可用操作）
        if sum(tiles) == 0:
            return False  # 当前玩家没有动作，输掉游戏

        # 尝试每种可能的操作
        for i in range(4):  # 4 种颜色
            if tiles[i] > 0:
                # 尝试移除一个该颜色的瓷砖
                new_tiles = list(tiles)
                new_tiles[i] -= 1
                if not dfs(new_tiles):  # 如果移除后对方处于必输状态，当前玩家获胜
                    memo[tuple(new_tiles)] = True
                    return True

        # 如果没有任何操作能让对方处于必输状态，则当前玩家输了
        memo[tuple(tiles)] = False
        return False

    return dfs(tiles)


# 主函数
def game_winner():
    # 设置初始的瓷砖数量，每种颜色有3个瓷砖
    tiles = [3, 3, 3, 3]  # 4种颜色，每种3个瓷砖

    # 判断能否获胜，若返回True，则当前玩家能赢，否则不能
    if can_win(tiles):
        print("Player 1 can win")
    else:
        print("Player 2 can win")

# 执行
game_winner()
