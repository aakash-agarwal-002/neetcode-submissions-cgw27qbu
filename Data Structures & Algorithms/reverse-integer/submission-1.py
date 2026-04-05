class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        
        while x:
            res = res * 10 + x % 10
            x //= 10
        
        res *= sign
        
        return res if INT_MIN <= res <= INT_MAX else 0
