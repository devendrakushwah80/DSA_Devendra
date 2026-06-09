class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avg = [-1]*len(nums)
        for i in range(len(nums)):
            if i-k>=0 and i+k<len(nums):
                start = i-k
                end = i + k
                total = 0
                for j in range(start,end+1):
                    total += nums[j]
                avg[i] = total // (2*k + 1)
        return avg