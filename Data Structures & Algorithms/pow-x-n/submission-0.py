class Solution:
    def myPow(self, x: float, n: int) -> float:

        fact = 1
        if n<0: 
            fact = -1
            n = n*fact
        
        def power(n):
            if n==0:
                return 1
            if n==1:
                return x
            res = power(n//2)
            return res*res if n%2==0 else x*res*res
     

        
        res = power(n)
        if fact==-1:
            res = 1/res
        return res
