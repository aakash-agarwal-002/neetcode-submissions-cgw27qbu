class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alpha = [0]*26
        n = len(s)
        maxc = 0
        l,r=0,0
        while r<n:
            alpha[ord(s[r])-ord('A')]+=1
            curr =  max(alpha)
            while (r-l+1) - curr > k:
                alpha[ord(s[l])-ord('A')]-=1
                l+=1
            maxc = max(maxc,r-l+1)   
            r+=1
        return maxc