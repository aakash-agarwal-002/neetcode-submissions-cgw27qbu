class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def dp(i,target):
            if i >= n:
                if target == 0:
                    return 1
                return 0
            
            return dp(i+1, target-nums[i]) + dp(i+1, target+nums[i])

        return dp(0,target)