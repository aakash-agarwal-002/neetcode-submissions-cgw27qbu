class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = dict()
        for i in range(len(tasks)):
            d[tasks[i]] = d.get(tasks[i],0)+1
        
        tasks = [-a for a in d.values()]
        heapq.heapify(tasks)
        res = 0

        while len(tasks) > 0:
            pend = []
            for i in range(n + 1):
                if len(tasks) == 0 and len(pend) == 0:
                    break

                res += 1
                if len(tasks) > 0:
                    curr = heapq.heappop(tasks)
                    curr += 1
                    if curr < 0:
                        pend.append(curr)

            for x in pend:
                heapq.heappush(tasks, x)

            
        return res