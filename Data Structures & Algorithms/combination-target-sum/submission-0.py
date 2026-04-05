class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def solve(curr,nums,target):
            if target < 0 or len(nums)==0:
                return
            if target ==0:
                res.append(curr)
                return
            
            take = solve(curr+[nums[0]],nums,target-nums[0])
            leave = solve(curr,nums[1:],target)


        
        solve([],nums,target)

        return res