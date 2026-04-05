class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def sub(curr,nums):
            print(curr)
            if len(nums)==0:
                res.append(curr)
                return
            leave = sub(curr,nums[1:])
            take = sub(curr + [nums[0]],nums[1:])
        
        sub([],nums)
        return res
