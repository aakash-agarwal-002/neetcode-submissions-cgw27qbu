class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for idx, (i,j) in enumerate(intervals):
            if newInterval[0] < i and newInterval[1] < i:
                print("1")
                res.append(newInterval)
                return res + intervals[idx:]
                print(res)
            elif newInterval[0] > j and newInterval[1] > j:
                print("2")
                res.append([i,j])
                print(res)
            else:
                print("3")
                newInterval[0] = min(newInterval[0],i)
                newInterval[1] = max(newInterval[1],j)
                print(newInterval)
            
        res.append(newInterval)
        return res