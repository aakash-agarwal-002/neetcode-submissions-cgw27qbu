class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxs = -1000001
        for i in range(1,n+1):
            for j in range(n-i+1):
                maxs = max(sum(nums[j:j+i]),maxs)
        return maxs
                    
