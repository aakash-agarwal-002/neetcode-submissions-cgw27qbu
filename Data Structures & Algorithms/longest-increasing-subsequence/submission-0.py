class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0

        def dp(i,curr):
            nonlocal res
            if i >= len(nums):
                if len(curr) > res:
                    res = len(curr)
                return
                    
            leave = dp(i+1,curr)

            if len(curr)>0:
                if curr[-1] < nums[i]:
                    take = dp(i+1,curr+[nums[i]])
            else:
                    take = dp(i+1,curr+[nums[i]])

            pass

        dp(0,[])
        return res