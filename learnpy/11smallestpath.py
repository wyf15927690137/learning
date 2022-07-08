def minPathSum(grid) -> int:
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if i == j == 0:
                pass
            elif i == 0:
                grid[i][j] += grid[i][j - 1]
            elif j == 0:
                grid[i][j] += grid[i - 1][j]
            else:
                grid[i][j] += grid[i - 1][j] if grid[i - 1][j] < grid[i][j - 1] else grid[i][j - 1]
    return grid[-1][-1]


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

x = minPathSum(grid)
print(x)
