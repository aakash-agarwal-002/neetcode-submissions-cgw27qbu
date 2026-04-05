class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr,l,r):
            print(l,r)
            if len(curr) == 2*n and l==r:
                res.append(curr)
            
            if l<n:
                backtrack(curr + "(",l+1,r)
            
            if r<l:
                backtrack(curr + ")",l,r+1)


        
        backtrack("(",1,0)
        return res