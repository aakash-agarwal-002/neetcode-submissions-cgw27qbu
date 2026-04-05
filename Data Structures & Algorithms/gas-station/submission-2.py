class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        diff = [g-c for g,c in zip(gas,cost)]
        if sum(gas)<sum(cost):
            return -1
        total = 0
        start = 0

        for i in range(len(diff)):
            total+=diff[i]
            if total < 0:
                total = 0
                start = i+1
        return start