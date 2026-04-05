class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxs = nums[0]
        
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                maxs = max(maxs, curr)
        
        return maxs