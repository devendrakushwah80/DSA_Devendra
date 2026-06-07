class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        h = k-1
        count = 0
        for i in range(l,h+1):
            if s[i] in 'aeiou':
                count+=1
        res =count
        while h<len(s)-1:
            l+=1
            h+=1
            if s[l-1] in 'aeiou':
                count = count-1
            if s[h] in 'aeiou':
                count+=1
            res = max(res, count)
        return res