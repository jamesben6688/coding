from typing import List


def is_path_to_target(grid: List[List[int]], r1: int, c1: int, t: int, k: int) -> bool:
    m, n = len(grid), len(grid[0])

    # Directions for moving: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # To store the visited cells
    visited = [[False] * n for _ in range(m)]

    # DFS helper function
    def dfs(r, c):
        # If out of bounds or already visited, return False
        if r < 0 or r >= m or c < 0 or c >= grid[r] or visited[r][c]:
            return False

        # If we reach the target cell
        if grid[r][c] == t:
            return True

        # # If the current cell is not k, we can't move through it
        # if grid[r][c] != k:
        #     return False

        # Mark the current cell as visited
        visited[r][c] = True

        # Explore all four possible directions
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if grid[new_r][new_c] in [k, target] and not visited[new_r][new_c] and dfs(new_r, new_c):
                return True

        visited[r][c] = False
        return False

    # Start the DFS from the given starting cell
    return dfs(r1, c1)


# Example Usage
grid = [
    [1, 7, 7, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
start_row, start_col = 0, 0
target = 11
k = 7

result = is_path_to_target(grid, start_row, start_col, target, k)
print(result)  # Output: True or False
