class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, curr ):
            
            if sum(curr) == target:
                    res.append(curr.copy())
                    return
            
            if sum(curr)> target:
                return  
            
            for k in range(i,len(nums)):
                backtrack(k,curr+[nums[k]])

        backtrack(0, [])
        return res