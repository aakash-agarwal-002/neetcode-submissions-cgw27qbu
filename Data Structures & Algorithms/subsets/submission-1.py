class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def sub(nums,i,curr):
            if i>=len(nums):
                res.append(curr.copy())
                return
            print(curr)
            sub(nums,i+1,curr+[nums[i]])
            sub(nums,i+1,curr)

        sub(nums,0,[])
        return res
