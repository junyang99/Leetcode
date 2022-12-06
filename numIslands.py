def numIslands(grid):
    max_row = len(grid)
    max_col = len(grid[0])
    count = 0

    def check(r, c, count):
        if r < max_row & c < max_col:
            if r >= 1 * c >= 1:
                if grid[r][c] == 1 & grid[r-1][c] == 1 & grid[r+1][c] == 1 & grid[r][c+1] == 1 & grid[r][c-1] == 1:
                    count += 1
                    return count

    for r in range(max_row):
        for c in range(max_col):
            check(r, c, count)

    return count

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))