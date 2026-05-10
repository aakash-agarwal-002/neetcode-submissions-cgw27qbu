class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        xor = 0
        for i in nums:
            xor^=i
        print(xor)
        diff = xor&(-xor)
        left = []
        right = []
        for i in nums:
            if i&diff:
                left.append(i)
            else:
                right.append(i)
        xor = 0
        for i in left:
            xor ^= i
        res.append(xor)
        xor = 0
        for i in right:
            xor ^= i
        res.append(xor)
        return res
