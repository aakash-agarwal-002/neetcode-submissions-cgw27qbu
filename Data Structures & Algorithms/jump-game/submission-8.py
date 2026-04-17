class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        reach = 0
        for i in range(len(nums)-1):
            if reach < i:
                return False
            curr = nums[i] + i
            print(curr)
            if curr > reach:
                reach = curr
        if reach >= len(nums)-1:
            return True
        return False