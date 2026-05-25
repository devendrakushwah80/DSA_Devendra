class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split("|")
        count = 0
        for i in range(0,len(s),2):
            k = s[i]
            for j in k:
                if j =="*":
                    count+=1
        return count