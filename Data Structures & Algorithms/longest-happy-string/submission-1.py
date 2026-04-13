class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heap.append((-a, "a"))
        if b > 0:
            heap.append((-b, "b"))
        if c > 0:
            heap.append((-c, "c"))
        heapq.heapify(heap)
        res = []

        while heap:
            print(heap)
            if len(res)<2:
                temp = heapq.heappop(heap)
                res.append(temp[1])
                if temp[0]+1<0:
                    heapq.heappush(heap,(temp[0]+1,temp[1]))

            elif res[-1] == res[-2] and heap[0][1] == res[-1]:
                one = heapq.heappop(heap)
                if not heap:
                    return "".join(res)
                temp = heapq.heappop(heap)
                res.append(temp[1])
                if temp[0]+1<0:
                    heapq.heappush(heap,(temp[0]+1,temp[1]))
                heapq.heappush(heap,one)
            else:
                temp = heapq.heappop(heap)
                res.append(temp[1])
                if temp[0]+1<0:
                    heapq.heappush(heap,(temp[0]+1,temp[1]))

        return "".join(res)
