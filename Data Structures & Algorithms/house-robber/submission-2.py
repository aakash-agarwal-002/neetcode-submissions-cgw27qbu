class Solution:
    def rob(self, nums: List[int]) -> int:
        d = dict()
        def solve(i):
            if d.get(i,0):
                return d[i]
            if i >= len(nums):
                return 0 
            take = nums[i] + solve(i+2)
            leave = solve(i+1)
            d[i] = max(take, leave)
            return d[i]

        return solve(0)