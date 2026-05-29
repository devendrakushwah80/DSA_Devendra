class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq  = {}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] =1
        val = freq.values()
        Set = set(val)
        if len(Set)==len(val):
            return True
        return False