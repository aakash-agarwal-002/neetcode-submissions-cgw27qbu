class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            dist = points[i][0]*points[i][0] + points[i][1]*points[i][1]
            points[i] = [dist] + points[i]

        heapq.heapify(points)
        res = []

        while len(res)<k:
            a = heapq.heappop(points)
            res.append(a[1:])

        return res