class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        s = ""
        i = 0
        while i < min(len(word1),len(word2)):
            s = s + word1[i]
            s = s + word2[i]
            i+=1
        
        if len(word1) == len(word2):
            return s
        elif len(word1)<len(word2):
            return s + word2[i:]
        else:
            return s + word1[i:]