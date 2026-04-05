class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l,r = 0,1
        maxc = 0
        while r<n:
            maxc = max(maxc,prices[r]-prices[l])
            if prices[l]>prices[r]:
                l = r
                r = r+1
            else:
                r=r+1

        return maxc