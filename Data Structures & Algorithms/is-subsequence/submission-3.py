class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n==0:
            return True

        i=0
        j=0

        while i<m and j<n:
            if s[j]==t[i]:
                j+=1
            i+=1 
        return j==n