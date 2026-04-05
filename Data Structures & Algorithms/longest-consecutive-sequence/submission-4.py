class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxc = 0

        for i in nums:
            if i-1 in s:
                continue
            else:
                count = 0
                while i+count in s:
                    count+=1

                if count > maxc:
                    maxc = count
        return maxc