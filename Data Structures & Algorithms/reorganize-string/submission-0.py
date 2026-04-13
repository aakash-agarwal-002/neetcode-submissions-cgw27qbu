class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-v,k) for k,v in count.items()]
        heapq.heapify(heap)
        res = []
        while heap:
            v,k = heapq.heappop(heap)
            if len(res)>=1 and res[-1] == k:
                if not heap:
                    return ""

                v1,k1 = heapq.heappop(heap)
                res.append(k1)
                if v1+1<0:
                    heapq.heappush(heap,(v1+1,k1))
                heapq.heappush(heap,(v,k))
            else:
                res.append(k)
                if v+1<0:
                    heapq.heappush(heap,(v+1,k))


        return "".join(res)