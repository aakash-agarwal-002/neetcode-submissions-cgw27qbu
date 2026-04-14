class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_set = set()
        all_set = set([i for i in range(1,n+1)])
        judge = set()
        for i in trust:
            trust_set.add(i[0])
        for i in trust:
            judge.add(i[1])
        
        if len(judge) > 1:
            return -1
        if len(all_set - trust_set) > 1:
            return -1
        else:
            res = all_set - trust_set
            return res.pop()