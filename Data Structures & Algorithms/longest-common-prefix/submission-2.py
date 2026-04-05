class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr = 0
        l = 0

        while l<len(strs[0]):
            for i in range(1,len(strs)):
                if l < len(strs[i]) and strs[0][l] == strs[i][l]:
                    continue
                else:
                    return strs[0][:l]
            l+=1

        return strs[0]