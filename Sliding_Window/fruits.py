class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        freq = {}
        maxi = 0
        for r in range(len(fruits)):
            freq[fruits[r]] = freq.get(fruits[r],0)+1
            while len(freq)>2:
                freq[fruits[l]]-=1
                if freq[fruits[l]]==0:
                    del freq[fruits[l]]
                l+=1
            maxi = max(maxi ,r - l +1)
        return maxi
