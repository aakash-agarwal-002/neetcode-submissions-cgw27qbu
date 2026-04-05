class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def csum(i,curr):
            print(curr)
            if sum(curr)==target:
                res.append(curr)
                return
            if i>= len(nums) or sum(curr)>target:
                return

            csum(i,curr+[nums[i]])
            csum(i+1,curr)


        csum(0,[])
        return res
