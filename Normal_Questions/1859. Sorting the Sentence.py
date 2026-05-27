class Solution:
    def sortSentence(self, s: str) -> str:
        s =  s.split()
        res = [0]*len(s)
        for i in range(len(s)):
            curr = s[i]
            pos = curr[-1]
            res[int(pos)-1]= curr[:-1]
        return " ".join(res)