class Solution:
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(start, curr):
            print(curr)
            if start>=len(s):
                res.append(curr.copy())
            for i in range(start, len(s)):
                if self.isPalindrome(s[start:i+1]):
                    curr.append(s[start:i+1])
                    backtrack(i+1,curr)            
                    curr.pop()
        
        backtrack(0,[])
        return res