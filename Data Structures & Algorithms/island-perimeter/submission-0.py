class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = 0 
                if grid[i][j] == 1:
                    if i-1>=0 and grid[i-1][j] != 1 or i==0:
                        curr+=1
                    if j-1>=0 and grid[i][j-1] != 1 or j==0:
                        curr+=1
                    if i+1<len(grid) and grid[i+1][j] != 1 or i==len(grid)-1:
                        curr+=1
                    if j+1<len(grid[0]) and grid[i][j+1] != 1 or j==len(grid[0])-1:
                        curr+=1
                print(i,j,curr)
                peri+=curr
        return peri