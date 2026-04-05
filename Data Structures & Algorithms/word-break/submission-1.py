from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dp(start):
            if start == len(s):
                return True
            
            if start in memo.keys():
                return memo[start]
            
            for i in range(start, len(s)):
                if s[start:i+1] in wordDict:
                    if dp(i+1):
                        memo[start]= True
                        return memo[start]

            memo[start] = False
            return memo[start]

        return dp(0)