class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq1 ={}
        freq2 = {}
        res = []
        for i in p:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1
        l = 0
        h = len(p)-1
        for i in s[l:h+1]:
            if i in freq2:
                freq2[i]+=1
            else:
                freq2[i]=1
        if freq1 == freq2:
            res.append(l)
        while h<len(s)-1:
            remove = s[l]
            freq2[remove]-=1
            if freq2[remove]==0:
                del freq2[remove]
            l+=1
            h+=1

            add = s[h]
            freq2[add]=freq2.get(add,0)+1
            if freq2 ==freq1:
                res.append(l)
        return res
