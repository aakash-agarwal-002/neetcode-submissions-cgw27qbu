class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # start1 < start2
        i = 0
        while i < len(intervals)-1:
            start1 = intervals[i][0]
            end1 = intervals[i][1]
            start2 = intervals[i+1][0]
            end2 = intervals[i+1][1]
            if end1 >= start2:
                intervals[i] = [start1,max(end1,end2)]
                intervals.pop(i+1)
            else:
                i+=1
        return intervals