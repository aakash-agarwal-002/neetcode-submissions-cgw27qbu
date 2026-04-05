class Solution:
    def reverseBits(self, n: int) -> int:
        res = ""
        ans = 0
        i=1
        while i<=32:
            res = res + str(n%2)
            n=n//2
            i+=1
        print(res)
        for i in res:
            ans = 2*(ans) + int(i)
        return ans