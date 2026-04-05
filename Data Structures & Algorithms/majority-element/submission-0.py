class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i],0) + 1

        return max(d, key=d.get)