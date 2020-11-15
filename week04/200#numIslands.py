class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        x = 0
        if m == 0 or n == 0:
            return x
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    x += 1
        return x

    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        print(i, j)
        if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
            grid[i][j] = "0"
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)