class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n<0: 
            x = 1/x
            n = -n
        
        def power(n):
            if n==0:
                return 1
            if n==1:
                return x
            res = power(n//2)
            return res*res if n%2==0 else x*res*res

        return power(n)
