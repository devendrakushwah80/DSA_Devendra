class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count =len(intervals)
        c = intervals[0][0]
        d = intervals[0][1]
        for i in range(1,len(intervals)):
            a = intervals[i][0]
            b  = intervals[i][1]
            if c <= a and b <= d:
                count-=1
            else:
                c = a
                d = b
        return count