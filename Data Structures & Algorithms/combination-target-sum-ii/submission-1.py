class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        def solve(curr,candidates,target):
            print(curr)
            if target == 0:
                res.add(tuple(curr))
                return
            if target < 0 or len(candidates)==0:
                return
            
            take = solve(curr+[candidates[0]],candidates[1:],target-candidates[0])
            leave = solve(curr,candidates[1:],target)

        
        solve([],candidates,target)

        return [list(a) for a in res]      