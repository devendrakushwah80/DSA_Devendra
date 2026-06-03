class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s =list(s)
        t = list(t)
        res1 = []
        res2 = []
        for i in range(len(s)):
            if s[i]!="#":
                res1.append(s[i])
            else:
                if res1:
                    res1.pop()
        for i in range(len(t)):
            if t[i]!="#":
                res2.append(t[i])
            else:
                if res2:
                    res2.pop()
        if "".join(res1)=="".join(res2):
            return True
        return False