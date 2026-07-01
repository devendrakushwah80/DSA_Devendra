class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=0
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if end>s:
                count+=1
                end = min(end,e)
            else:
                end = e
        return count