class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low = 0
        zeros = 0
        maxlen = 0
        for high in range(len(nums)):
            if nums[high]==0:
                zeros +=1
            while zeros>k:
                if nums[low]==0:
                    zeros-=1
                low+=1
            if zeros<=k:
                length = high-low+1
                maxlen = max(maxlen,length)
        return maxlen