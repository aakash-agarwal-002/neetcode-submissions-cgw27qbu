class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix  = [height[0]]*n
        suffix  = [height[n-1]]*n
        res = 0

        for i in range(1,n):
            prefix[i] = max(prefix[i-1],height[i])
            suffix[n-i-1] = max(suffix[n-i],height[n-i-1])
        for i in range(1,n):
            temp = min(prefix[i],suffix[i])-height[i]
            res += temp if temp > 0 else 0

        return res

        

        