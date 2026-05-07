class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res = res + str(len(i)) + "_" + i
        print(strs)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        digit = ""
        while i < len(s):
            while s[i]!="_":
                digit = digit + s[i]
                i+=1
            print(digit)
            start = i+1
            end = int(digit) + start
            # print(s[i],start,end)
            curr = s[start:end]
            # print(curr)
            res.append(curr)
            i=end
            digit = ""

        return res
