class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)  
        res = [False]      

        def solve(curr):
            if curr == n-1:
                res[0] = True
                return
            if curr > n-1:
                return
            for j in range(1,nums[curr]+1):
                if solve(curr+j):
                    return

        solve(0)
        return res[0]
