class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False

        # remove last set bit incase of PowerOfTwo it is the only bit
        clear = n&(n-1) 
        if not clear:
            return True
        else:
            return False