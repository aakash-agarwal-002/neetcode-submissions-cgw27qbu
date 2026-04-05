class Solution:
    def dfs(self,i,j,grid,visited):
        rows = len(grid)
        cols = len(grid[0])
        if  j+1<cols and visited[i][j+1]!=1 and grid[i][j+1]=="1":
            visited[i][j+1]=1
            self.dfs(i,j+1,grid,visited)
        if i-1>=0 and visited[i-1][j]!=1 and grid[i-1][j]=="1":
            visited[i-1][j]=1
            self.dfs(i-1,j,grid,visited)
        if j-1>=0 and visited[i][j-1]!=1 and grid[i][j-1]=="1":
            visited[i][j-1]=1
            self.dfs(i,j-1,grid,visited)
        if i+1<rows and visited[i+1][j]!=1 and grid[i+1][j]=="1":
            visited[i+1][j]=1
            self.dfs(i+1,j,grid,visited)
            

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and visited[i][j]!=1:
                    count+=1
                    visited[i][j]=1
                    self.dfs(i,j,grid,visited)

        return count



