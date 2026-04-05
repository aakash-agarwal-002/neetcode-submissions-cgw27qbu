class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr,used):

            if len(curr)==len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    backtrack(curr+[nums[i]],used)
                    used[i] = False

        used = [False]*len(nums)
        backtrack([],used)
        return res