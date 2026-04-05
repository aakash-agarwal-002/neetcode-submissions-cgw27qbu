class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        memo = {}

        def dp(i, prev):
            if i == n:
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]

            leave = dp(i + 1, prev)

            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + dp(i + 1, i)

            memo[(i, prev)] = max(leave, take)
            return memo[(i, prev)]

        return dp(0, -1)