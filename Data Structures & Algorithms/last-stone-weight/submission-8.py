class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-a for a in stones]
        heapq.heapify(stones)
        print(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x>y:
                heapq.heappush(stones,-(x-y))
            elif y>x:
                heapq.heappush(stones,-(y-x))
        
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
