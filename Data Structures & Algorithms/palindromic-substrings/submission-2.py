class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        def ispalindrome(l, r):
            if l >= r:
                return True
            if s[l] != s[r]:
                return False
            return ispalindrome(l + 1, r - 1)
        
        def count(start):
            if start == n:
                return 0
            
            total = 0
            for end in range(start, n):
                if ispalindrome(start, end):
                    total += 1
            
            return total + count(start + 1)
        
        return count(0)