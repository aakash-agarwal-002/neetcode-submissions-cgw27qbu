class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        s = set()

        j=0
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
                nums[j] = nums[i]
                j+=1

        return j

            