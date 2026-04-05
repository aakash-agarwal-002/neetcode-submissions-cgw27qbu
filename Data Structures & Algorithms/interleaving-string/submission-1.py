from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        o = len(s3)

        if m+n != o:
            return False

        @lru_cache(None)
        def dp(i,j,k):
            print(i,j,k)
            if i==m and j==n and i+j==k:
                return True
            
            
            res1 = False
            res2 = False
            if i<m and s1[i] == s3[k]:
                res1 = dp(i+1,j,k+1)
            if j<n and s2[j] == s3[k]:
                res2 = dp(i,j+1,k+1)
            return res1 or res2

        return dp(0,0,0)