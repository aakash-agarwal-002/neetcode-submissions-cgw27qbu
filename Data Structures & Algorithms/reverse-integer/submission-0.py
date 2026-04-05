class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        isnegative = True if x<0 else False
        x = abs(x)
        while x>0:
            res = res*10 + x%10
            x//=10
        res =  -res if isnegative else res
        if res < INT_MIN or res > INT_MAX:
            return 0
        return res