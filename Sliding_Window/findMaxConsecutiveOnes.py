class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        maxi = 0
        for high in range(len(nums)):
            if nums[high] == 1:
                ones += 1
                maxi = max(maxi, ones)
            else:
                ones = 0
        return maxi