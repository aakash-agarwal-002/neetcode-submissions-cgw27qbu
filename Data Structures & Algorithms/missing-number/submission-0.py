class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)+1
        miss = int(n*(n-1)/2)
        return miss - sum(nums) 