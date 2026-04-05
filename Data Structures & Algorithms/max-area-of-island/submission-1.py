class Solution:
    def dfs(self, i, j, grid, visited):
        rows = len(grid)
        cols = len(grid[0])

        if i < 0 or i >= rows or j < 0 or j >= cols:
            return 0
        if visited[i][j] == 1 or grid[i][j] == 0:
            return 0

        visited[i][j] = 1
        count = 1

        count += self.dfs(i, j + 1, grid, visited)
        count += self.dfs(i - 1, j, grid, visited)
        count += self.dfs(i, j - 1, grid, visited)
        count += self.dfs(i + 1, j, grid, visited)

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    res = max(res, self.dfs(i, j, grid, visited))

        return res
