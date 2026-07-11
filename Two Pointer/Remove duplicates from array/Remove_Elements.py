class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for h in range(len(nums)):
            if nums[h]!=val:
                nums[l],nums[h]=nums[h],nums[l]
                l+=1
        l = 0 
        while l<len(nums):
            if nums[l]==val:
                nums.pop(l)
            else:
                l+=1
        return len(nums) 
