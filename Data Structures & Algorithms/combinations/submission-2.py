class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dp(start, used):
            if len(used) == k:
                res.append(used.copy())
                return
                
            for i in range(start, n + 1):
                used.append(i)
                dp(i + 1, used)
                used.pop()
        
        dp(1, [])
        return res