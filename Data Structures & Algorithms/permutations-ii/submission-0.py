class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(used,curr):
            print(curr)
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i]=True
                backtrack(used,curr+[nums[i]])
                used[i]=False
        
        used = [False]*len(nums)
        backtrack(used,[])
        return res
