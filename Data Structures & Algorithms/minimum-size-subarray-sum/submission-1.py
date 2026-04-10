class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums)<target:
            return 0

        curr_sum = 0
        res = len(nums)
        l = 0 
        r = 0

        while l<=r and r<len(nums):
            curr_sum+= nums[r]
            while curr_sum>=target:
                if r-l+1 < res:
                    res =  r-l+1
                curr_sum-=nums[l]
                l+=1
            r+=1

        return res