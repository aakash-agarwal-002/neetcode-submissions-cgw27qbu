class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)  
        maxreach = 0
        for i in range(0,n):
            if i > maxreach:
                return False
            maxreach = max(maxreach,nums[i]+i)
            print(maxreach)
        return True
