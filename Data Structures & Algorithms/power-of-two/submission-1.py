class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        clear = n&(n-1)
        print(clear)
        if not clear:
            return True
        else:
            return False