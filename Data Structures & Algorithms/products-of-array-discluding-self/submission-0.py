class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [0]*(len(nums))
        suffix = [0]*(len(nums))

        for i,n in enumerate(nums):
            if i==0:
                prefix[i] = n
            else:
                prefix[i] = n*prefix[i-1]

        for i,n in enumerate(nums[::-1]):
            if i==0:
                suffix[len(nums) - i -1] = n
            else:
                suffix[len(nums) - i -1] = n*suffix[len(nums) - i]

        print(prefix)
        print(suffix)
    
        for i,n in enumerate(nums):
            left = prefix[i - 1] if i > 0 else 1
            right = suffix[i + 1] if i < len(nums) - 1 else 1
            nums[i] = left * right

        return nums