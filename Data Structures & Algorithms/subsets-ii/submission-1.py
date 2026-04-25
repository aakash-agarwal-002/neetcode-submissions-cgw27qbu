class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start,curr):
            res.append(curr.copy())
            
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                backtrack(i+1,curr+[nums[i]])
        backtrack(0,[])

        return res