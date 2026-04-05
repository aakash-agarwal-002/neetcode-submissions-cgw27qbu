class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        def dp(i,j):
            print(i,j)
            res = 0
            if i>=m or j>=n or i<0 or j<0:
                return 0
            if i+1<m and matrix[i+1][j]>matrix[i][j]:
                res = max(res,1 + dp(i+1,j))
            if j+1<n and matrix[i][j+1]>matrix[i][j]:
                res = max(res,1 + dp(i,j+1))
            if i-1>=0 and matrix[i-1][j]>matrix[i][j]:
                res = max(res,1 + dp(i-1,j))
            if j-1>=0 and matrix[i][j-1]>matrix[i][j]:
                res = max(res,1 + dp(i,j-1))
            return res

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res,dp(i,j))
        return res+1