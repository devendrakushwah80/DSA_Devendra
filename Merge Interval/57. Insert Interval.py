class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = intervals.copy()
        res.append(newInterval)
        res.sort()
        ans = []
        start = res[0][0]
        end = res[0][1]
        for i in range(1,len(res)):
            s = res[i][0]
            e = res[i][1]
            if end>=s:
                end = max(end,e)
            else:
                ans.append([start,end])
                start = s
                end =e 
        ans.append([start,end])
        return ans