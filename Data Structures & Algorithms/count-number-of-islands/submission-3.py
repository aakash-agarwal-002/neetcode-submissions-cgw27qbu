class Solution:
    def dfs(self, i, j, grid, visited):
        rows = len(grid)
        cols = len(grid[0])

        if i < 0 or i >= rows or j < 0 or j >= cols:
            return
        if visited[i][j] == 1 or grid[i][j] == "0":
            return

        visited[i][j] = 1

        self.dfs(i, j + 1, grid, visited)
        self.dfs(i - 1, j, grid, visited)
        self.dfs(i, j - 1, grid, visited)
        self.dfs(i + 1, j, grid, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    count += 1
                    self.dfs(i, j, grid, visited)

        return count
