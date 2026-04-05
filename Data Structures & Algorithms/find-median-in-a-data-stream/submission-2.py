import heapq

class MedianFinder:

    def __init__(self):
        self.h1 = []  # max heap (negative values)
        self.h2 = []  # min heap

    def addNum(self, num: int) -> None:
        # step 1: push into appropriate heap
        if not self.h1 or num <= -self.h1[0]:
            heapq.heappush(self.h1, -num)
        else:
            heapq.heappush(self.h2, num)

        # step 2: rebalance (only one move ever needed)
        if len(self.h1) > len(self.h2) + 1:
            heapq.heappush(self.h2, -heapq.heappop(self.h1))
        elif len(self.h2) > len(self.h1) + 1:
            heapq.heappush(self.h1, -heapq.heappop(self.h2))

    def findMedian(self) -> float:
        if len(self.h1) == len(self.h2):
            return (-self.h1[0] + self.h2[0]) / 2
        elif len(self.h1) > len(self.h2):
            return -self.h1[0]
        else:
            return self.h2[0]
