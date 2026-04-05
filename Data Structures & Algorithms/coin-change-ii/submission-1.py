from functools import lru_cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)

        @lru_cache(None)
        def dp(i,target):
            if i >= n:
                return 0

            if target < 0:
                return 0
            
            if target == 0:
                return 1
            
            return dp(i,target-coins[i]) + dp(i+1,target)

        return dp(0, amount)
