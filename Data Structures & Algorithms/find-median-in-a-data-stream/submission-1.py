class MedianFinder:

    def __init__(self):
        self.h1 = []
        self.h2 = []
        self.len_h1 = 0
        self.len_h2 = 0
        

    def addNum(self, num: int) -> None:
        if len(self.h1)==0:
            heapq.heappush(self.h1,-num)
            self.len_h1 +=1
        elif num <= -self.h1[0]: 
            heapq.heappush(self.h1,-num)
            self.len_h1 +=1
        else:
            heapq.heappush(self.h2,num)
            self.len_h2+=1

        if abs(self.len_h1 - self.len_h2) > 1:
            if self.len_h1 > self.len_h2:
                while abs(self.len_h1 - self.len_h2) > 1:
                    a = heapq.heappop(self.h1)
                    self.len_h1-=1
                    heapq.heappush(self.h2,-a)
                    self.len_h2+=1

            else:
                while abs(self.len_h1 - self.len_h2) > 1:
                    a = heapq.heappop(self.h2)
                    self.len_h2-=1
                    heapq.heappush(self.h1,-a)
                    self.len_h1+=1
                
        


    def findMedian(self) -> float:
        print(self.h1)
        print(self.h2)
        if self.len_h1 == self.len_h2 :
            return (-self.h1[0] + self.h2[0])/2
        elif self.len_h1 > self.len_h2:
            return -self.h1[0]
        else:
            return self.h2[0]

        
        