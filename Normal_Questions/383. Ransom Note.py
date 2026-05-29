class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freqmag = {}
        freqran ={}
        for i in ransomNote:
            if i in freqran:
                freqran[i]+=1
            else:
                freqran[i]= 1
        for i in magazine:
            if i in freqmag:
                freqmag[i]+=1
            else:
                freqmag[i]= 1
        for i in freqran:
            if i not in freqmag:
                return False
            if freqran[i]>freqmag[i]:
                return False
        return True