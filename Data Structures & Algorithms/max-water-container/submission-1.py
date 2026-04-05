class Solution:
    # Brute force
    def maxArea_brute(self, heights: List[int]) -> int:
        maxc = -1
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                curr = (j-i)*min(heights[i],heights[j])
                maxc = max(maxc,curr)

        return maxc

    def maxArea(self, heights: List[int]) -> int:
        maxc = -1
        l,r = 0,len(heights)-1
        while l<r:
            curr = (r-l)*min(heights[l],heights[r])
            maxc = max(maxc,curr)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return maxc
    
    
        