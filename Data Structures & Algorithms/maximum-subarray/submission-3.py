class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxs = -1000001
        curr = 0
        for i in range(0,n):
            curr = curr + nums[i]
            maxs = max(curr,maxs)
            if curr < 0:
                curr = 0
        return maxs
