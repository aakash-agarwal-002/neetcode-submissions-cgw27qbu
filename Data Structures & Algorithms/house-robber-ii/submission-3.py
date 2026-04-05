class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0

        d_true = {}
        d_false = {}

        def dp(i,start):
            if i>= len(nums):
                return 0
            if i == len(nums)-1 and start:
                return 0

            if start:
                if i in d_true.keys():
                    return d_true[i]
            else:
                if i in d_false.keys():
                    return d_false[i]

            if start:
              d_true[i] = max(nums[i]+dp(i+2,start),dp(i+1,start))
              return d_true[i]
            else:
              d_false[i] = max(nums[i]+dp(i+2,start),dp(i+1,start))
              return d_false[i]

        res = max(dp(0,True),dp(1,False))
        return nums[0] if len(nums)==1 else res
