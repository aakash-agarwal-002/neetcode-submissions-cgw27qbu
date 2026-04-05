class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dp(i,j):
            if i==m-1 and j==n-1:
                return 1
            if i > m-1 or j>n-1:
                return 0
            
            res = 0
            res+= dp(i+1,j)
            res+= dp(i,j+1)
            return res
        return dp(0,0)