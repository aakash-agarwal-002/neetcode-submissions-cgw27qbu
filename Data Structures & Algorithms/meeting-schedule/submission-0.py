"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        i=0
        res = 0
        while i < len(intervals)-1:
            print(intervals[i].start,intervals[i].end)
            print(intervals[i+1].start,intervals[i+1].end)
            start1,end1 = intervals[i].start,intervals[i].end
            start2,end2 = intervals[i+1].start,intervals[i+1].end

            if end1 > start2:
                return False
            i+=1

        return True