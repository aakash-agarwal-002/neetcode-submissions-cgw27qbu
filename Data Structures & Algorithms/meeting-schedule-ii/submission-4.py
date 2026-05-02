"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [i.start for i in intervals]
        starts.sort()
        ends = [i.end for i in intervals]
        ends.sort()
        res = 0
        max_res = 0
        i=0
        j=0
        while i < len(starts) and j< len(starts):
            if starts[i] < ends[j]:
                res+=1
                max_res = max(res,max_res)
                i+=1
            else:
                res-=1
                j+=1
        return max_res




