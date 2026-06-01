class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        child = 0
        count = 0
        cookie = 0
        s.sort()
        g.sort()
        while child < len(g) and cookie < len(s):
            if s[cookie]>=g[child]:
                count+=1
                child+=1
                cookie+=1
            else:
                cookie+=1
        return count