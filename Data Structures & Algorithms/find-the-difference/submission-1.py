class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        com = s+t
        xor = 0
        for i in com:
            xor^=ord(i)
        return chr(xor)
