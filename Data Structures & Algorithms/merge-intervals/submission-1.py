class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0

        while i < len(intervals) - 1:
            start1, end1 = intervals[i]
            start2, end2 = intervals[i + 1]

            if end1 >= start2:
                intervals[i] = [start1, max(end1, end2)]
                intervals.pop(i + 1)
            else:
                i += 1

        return intervals