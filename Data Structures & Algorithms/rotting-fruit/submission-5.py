class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
        count=0
        while q:
            print(q)
            l = []
            for k in range(len(q)):
                i,j = q.popleft()
                if i-1>=0  and grid[i-1][j]==1:
                    grid[i-1][j]=2
                    l.append((i-1,j))
                if j-1>=0  and grid[i][j-1]==1:
                    grid[i][j-1]=2
                    l.append((i,j-1))
                if i+1<rows  and grid[i+1][j]==1:
                    grid[i+1][j]=2
                    l.append((i+1,j))
                if j+1<cols  and grid[i][j+1]==1:
                    grid[i][j+1]=2
                    l.append((i,j+1))
            
            q.extend(l)
            count+=1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return 0 if count==0 else count-1
