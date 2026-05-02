class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[1])
        i=0
        res = 0
        while i < len(intervals)-1:
            start1,end1 = intervals[i]
            start2,end2 = intervals[i+1]

            if end1 > start2:
                intervals.pop(i+1)
                res+=1
            else:
                i+=1

        return res