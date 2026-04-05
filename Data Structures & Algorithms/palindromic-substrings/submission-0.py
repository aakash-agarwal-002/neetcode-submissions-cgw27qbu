class Solution:
    def ispalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def countSubstrings(self, s: str) -> int:
        res = 0
        for l in range(1,len(s)+1):
            for i in range(0,len(s)-l+1):
                if self.ispalindrome(s[i:i+l]):
                    res+=1
        return res