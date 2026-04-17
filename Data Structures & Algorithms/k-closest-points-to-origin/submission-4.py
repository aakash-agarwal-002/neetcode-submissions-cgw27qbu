class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i,j in points:
            dist = i*i+j*j
            heapq.heappush(heap,(dist, [i,j]))
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res