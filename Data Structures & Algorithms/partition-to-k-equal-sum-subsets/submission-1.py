class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k !=0:
            return False
        target = sum(nums)//k
        bucket = [0]*k

        nums.sort(reverse=True)

        def backtrack(i):
            if i==len(nums):
                return True
            
            for j in range(k):
                if bucket[j] + nums[i]<=target:
                    bucket[j]+=nums[i]
                    if backtrack(i+1):
                        return True
                    bucket[j]-=nums[i]
                
                if bucket[j] == 0:
                    break
            return False
        return backtrack(0)