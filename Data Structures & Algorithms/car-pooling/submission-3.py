import heapq

class Solution:
    def carPooling(self, trips, capacity):
        trips.sort(key=lambda x: x[1])
        
        heap = []  # (end_location, passengers)
        curr = 0

        for passengers, start, end in trips:
            
            # Drop off passengers first
            while heap and heap[0][0] <= start:
                e, p = heapq.heappop(heap)
                curr -= p

            # Add current passengers
            curr += passengers

            if curr > capacity:
                return False

            heapq.heappush(heap, (end, passengers))

        return True