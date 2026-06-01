class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        h = 1
        while h<len(nums):
            if nums[h]!=nums[l]:
                nums[l+1]=nums[h]
                l+=1
                h+=1
            else:
                h+=1
        return l+1

