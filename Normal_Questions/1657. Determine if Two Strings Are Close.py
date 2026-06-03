class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = {}
        freq2 ={}
        for i in word1:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1
        for i in word2:
            if i in freq2:
                freq2[i]+=1
            else:
                freq2[i]=1
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        val1 =sorted(freq1.values())
        val2=sorted(freq2.values())
        if val1!=val2:
            return False
        return True