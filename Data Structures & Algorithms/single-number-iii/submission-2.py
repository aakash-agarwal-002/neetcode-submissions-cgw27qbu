class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor^=i
        print(xor)
        diff = xor&(-xor)
        left = 0
        right = 0
        for i in nums:
            if i&diff:
                left^=i
            else:
                right^=i
        return [left,right]
