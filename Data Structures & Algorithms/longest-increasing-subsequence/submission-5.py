from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        @lru_cache(None)
        def dp(i,prev):
            if i >= len(nums):
                return 0
                    
            leave = dp(i+1,prev)
            take = 0
            if prev == -1:
                prev = i
                take = 1+ dp(i,prev)
            elif prev !=-1 and nums[prev] < nums[i]:
                prev = i
                take = 1+ dp(i,prev)

            return max(leave,take)

        return dp(0,-1)