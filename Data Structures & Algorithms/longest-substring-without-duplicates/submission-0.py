class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l,r=0,0
        myset = set()
        maxc = 0
        while r<n:
            if s[r] not in myset:
                myset.add(s[r])
                r+=1
            
            else:
                while l<r and s[r] in myset:
                    myset.remove(s[l])
                    l+=1
                myset.add(s[r])
                r+=1
            maxc = max(maxc,r-l)

        return maxc

