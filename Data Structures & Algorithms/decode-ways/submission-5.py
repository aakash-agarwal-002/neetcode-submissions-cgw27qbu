class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0

        def dp(start):
            nonlocal res
            if start > len(s):
                return
            if start == len(s):
                res+=1
                return
            
            if s[start:start+1]!="0":
                dp(start+1)
            print(s[start:2])
            if s[start:start+2] and 10 <= int(s[start:start+2])<=26:
                dp(start+2)
            pass
        
        dp(0)
        return res