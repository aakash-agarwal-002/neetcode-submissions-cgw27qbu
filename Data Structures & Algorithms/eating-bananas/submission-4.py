class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 0

        while l<=r:
            mid = (l+r)//2
            k = 0
            for i in range(len(piles)):
                k+= math.ceil(piles[i]/mid)
            if k <= h:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans