class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        while l<=h:
            m=(l+h)//2
            if nums[m]>nums[len(nums)-1]:
                l=m+1
            else:
                res=m
                h=m-1
        return nums[res]
