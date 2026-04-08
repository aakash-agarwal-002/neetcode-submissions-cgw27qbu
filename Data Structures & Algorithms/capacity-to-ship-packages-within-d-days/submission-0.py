class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            d = 1
            curr = 0
            
            for w in weights:
                if curr + w <= capacity:
                    curr += w
                else:
                    d += 1
                    curr = w
                    
            return d <= days

        low = max(weights)
        high = sum(weights)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            
            if canShip(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans