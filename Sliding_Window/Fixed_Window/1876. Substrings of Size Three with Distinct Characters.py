class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        freq = {}
        l = 0 
        h = 3-1
        res = 0
        for i in s[l:h+1]:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        if len(freq)==3:
            res+=1
        else:
            res =0
        while h<len(s)-1:
            remove = s[l]
            freq[remove]-=1
            if freq[remove]==0:
                del freq[remove]
            l+=1
            h+=1

            add = s[h]
            freq[add] = freq.get(add, 0) + 1
            if len(freq) == 3:
                res += 1
        return res
            
