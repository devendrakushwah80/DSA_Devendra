class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] =1
        for i in freq:
            if freq[i]>(len(nums)/2):
                return i