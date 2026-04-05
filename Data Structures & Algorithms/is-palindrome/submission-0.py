class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for i in s:
            if i.isdigit() or i.isalpha():
                t = t + i.lower()
        return t[::-1] == t