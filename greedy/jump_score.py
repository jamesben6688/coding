def greedy_best_jump(arr):
    n = len(arr)
    score = 0
    path = [0]
    i = 0
    while i < n - 1:
        best_score = float('-inf')
        best_j = -1
        for j in range(i + 1, n):
            gain = arr[j] * (j - i)
            if gain > best_score:
                best_score = gain
                best_j = j
        score += best_score
        path.append(best_j)
        i = best_j
    return score, path


# print(greedy_best_jump(arr = [1, 200, 1, 1, 1, 1, 1000]))
print(greedy_best_jump(arr=[1, 20, 100, 30, 20, 10, 40]))  # 100*2+40*4=360
