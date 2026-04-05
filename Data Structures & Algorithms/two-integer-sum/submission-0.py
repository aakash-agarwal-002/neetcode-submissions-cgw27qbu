class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set()
        res = []
        for i,n in enumerate(nums):
            if target - n in s:
                print(n)
                res.append(i)
                break
            s.add(n)
        print(res)
        for i,n in enumerate(nums):
            if target - nums[res[0]] == nums[i]:
                print(i)
                res.insert(0,i)
                break
        return res