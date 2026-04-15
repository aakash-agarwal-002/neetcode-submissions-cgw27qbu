class Solution:
    def kadane(self, nums) -> int:
        curr = 0
        res = max(nums)
        for i in range(len(nums)):
            curr += nums[i]
            if res < curr:
                res = curr
            if curr < 0:
                curr = 0
        print(res)
        return res



    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        print(total)
        neg_nums = [-i for i in nums]
        max_kadane = self.kadane(nums)
        if max_kadane < 0:
            return max_kadane
        return max(max_kadane,total + self.kadane(neg_nums))

