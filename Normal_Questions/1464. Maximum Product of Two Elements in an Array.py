class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        h = len(nums)-1
        l = len(nums)-2
        return (nums[l]-1)*(nums[h]-1)