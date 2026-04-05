class Solution:
    def jump(self, nums: List[int]) -> int:
        q = deque()
        res = 0
        q.append((0,nums[0]))
        done = 0
        while q:
            print(q)
            n = len(q)
            maxl = -1
            while n > 0:
                index,jump = q.popleft()
                done = index
                maxl = max(index+jump, maxl)
                n-=1
            print(maxl)
            for i in range(done+1,min(maxl+1,len(nums))):
                q.append((i,nums[i]))
            res+=1
        
        return res-1
                

