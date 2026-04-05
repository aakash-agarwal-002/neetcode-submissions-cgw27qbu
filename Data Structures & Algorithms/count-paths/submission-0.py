class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def fact(num):
            if num == 0:
                return 1
            if num == 1: 
                return 1
            return num*fact(num-1)
        return int(fact(m+n-2)/(fact(m-1)*fact(n-1)))