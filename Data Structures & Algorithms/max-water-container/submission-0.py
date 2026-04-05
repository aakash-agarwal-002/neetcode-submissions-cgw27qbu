class Solution:
    # Brute force
    def maxArea(self, heights: List[int]) -> int:
        maxc = -1
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                curr = (j-i)*min(heights[i],heights[j])
                maxc = max(maxc,curr)

        return maxc
        