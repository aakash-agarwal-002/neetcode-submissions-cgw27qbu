class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mine = 10000

        while l<=r:
            mid = (l+r)//2
            if mine > nums[mid]:
                mine = nums[mid]

            if nums[mid] >= nums[r]:
                l = mid+1

            else:
                r = mid-1

        return mine

                

