class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s):
            l = 0
            r = len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        def backtracking(curr,start):
            if start>=len(s):
                res.append(curr.copy())

            for i in range(start,len(s)):
                if isPalindrome(s[start:i+1]):
                    curr.append(s[start:i+1])
                    backtracking(curr,i+1)
                    curr.pop()
            pass

        backtracking([],0)
        return res