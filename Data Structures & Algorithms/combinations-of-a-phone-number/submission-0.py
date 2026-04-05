class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        d = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        def backtrack(start,curr):
            if start >= len(digits):
                res.append(curr)
                return

            for  i in range(len(d[digits[start]])):
                backtrack(start+1,curr+d[digits[start]][i])

        backtrack(0,"")
        return [] if len(res)==1 and res[0] == "" else res