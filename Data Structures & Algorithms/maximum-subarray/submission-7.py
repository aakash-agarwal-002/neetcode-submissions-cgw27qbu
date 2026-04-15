class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = min(nums)
        curr = 0
        for i in range(len(nums)):
            curr+=nums[i]
            if curr > res:
                res = curr
            if curr < 0:
                curr = 0
        return res