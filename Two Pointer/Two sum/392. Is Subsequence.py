class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        h = 0
        while l<len(s) and h<len(t):
            if s[l]!=t[h]:
                h+=1
            else:
                l+=1
                h+=1
        if l ==len(s):
            return True
        return False