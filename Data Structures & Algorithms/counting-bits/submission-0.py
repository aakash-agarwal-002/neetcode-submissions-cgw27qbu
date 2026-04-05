class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        j = 0
        for i in range(n+1):
            while i>0:
                res[j] = res[j]+i%2
                i = i//2
            j+=1

        return res