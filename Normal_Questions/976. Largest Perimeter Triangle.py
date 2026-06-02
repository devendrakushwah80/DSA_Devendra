class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        peri = 0
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]>nums[i+2]:
                Sum = nums[i]+nums[i+1]+nums[i+2]
                if Sum >peri:
                    peri = Sum
        return peri