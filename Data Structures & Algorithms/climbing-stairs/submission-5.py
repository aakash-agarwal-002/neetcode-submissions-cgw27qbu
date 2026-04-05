class Solution:
    
    def rec(self,n,res):
        if res[n]!=-1:
            return res[n]
        if n==1 or n==2:
            return n
        if n<1:
            return 0

        res[n]= self.rec(n-1,res) + self.rec(n-2,res)
        return res[n]
        
    def climbStairs(self, n: int) -> int:
        res = [-1]*(n+1)
        return self.rec(n,res)
        