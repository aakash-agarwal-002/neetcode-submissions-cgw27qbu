class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        print(nums)
        n = len(nums)
        i = 0
        while i<n-k:
            heapq.heappop(nums)
            i+=1
        
        return nums[0]