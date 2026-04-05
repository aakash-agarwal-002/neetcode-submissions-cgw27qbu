class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        
        def dp(i,s1,s2):
            if i == len(nums):
                if sum(s1)==sum(s2):
                    return True
                return False

            return dp(i+1,s1+[nums[i]],s2) or dp(i+1,s1,s2+[nums[i]])

        return dp(0,[],[])