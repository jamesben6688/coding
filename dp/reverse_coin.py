def reverse_coin_dp(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    dp[0] = 1
    coins = [0] * (n + 1)

    for j in range(n):
        coin_found = False
        for i in range(1, n):
            """
                arr[i] - dp[i] == 1很关键。就是表明当前的amount由1个新的硬币组成
            """
            if not coin_found and arr[i] - dp[i] == 1:
                coin_found = True
                coins[j] = i

            if coin_found and i >= coins[j]:
                dp[i] += dp[i - coins[j]]

        if not coin_found:
            break

    for j in range(n):
        if dp[j] != arr[j]:
            print("NONE")
            return

    print(coins)
    for coin in coins:
        if coin != 0:
            print(coin)


# 示例测试
arr = [1, 0, 1, 0, 1, 1, 2, 1, 2, 1, 3]
reverse_coin_dp(arr)
