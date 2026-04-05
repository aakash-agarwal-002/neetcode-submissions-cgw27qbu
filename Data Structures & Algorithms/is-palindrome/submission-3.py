class Solution:
    def isPalindrome_1(self, s: str) -> bool:
        t = ""
        for i in s:
            if i.isdigit() or i.isalpha():
                t = t + i.lower()
        return t[::-1] == t
    
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for i in s:
            if i.isdigit() or i.isalpha():
                t = t + i.lower()
        l = 0
        r = len(t)-1
        while l<r:
            if t[l]!=t[r]:
                return False
            else:
                l+=1
                r-=1
        return True