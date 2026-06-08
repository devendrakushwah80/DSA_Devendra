class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        freq2 ={}
        if len(s1)>len(s2):
            return False
        for i in s1:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        l = 0
        h = len(s1)-1 
        for i in s2[:h+1]:
            if i in freq2:
                freq2[i]+=1
            else:
                freq2[i]=1
        if freq==freq2:
            return True
        while h<len(s2)-1:
            remove = s2[l]
            freq2[remove]-=1
            if freq2[remove]==0:
                del freq2[remove]
            l+=1
            h+=1

            add = s2[h]
            freq2[add]=freq2.get(add,0)+1
            if freq2 ==freq:
                return True
        return False