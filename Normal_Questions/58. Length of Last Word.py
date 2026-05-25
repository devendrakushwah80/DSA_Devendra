class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = list(s.split())
        i = s[len(s)-1]
        count = 0
        for j in i:
            count +=1
        return count