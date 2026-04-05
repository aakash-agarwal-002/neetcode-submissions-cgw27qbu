class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, curr):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            if sum(curr) > target:
                return

            for i in range(start, len(nums)):
                backtrack(i, curr + [nums[i]])
        backtrack(0,[])
        return res