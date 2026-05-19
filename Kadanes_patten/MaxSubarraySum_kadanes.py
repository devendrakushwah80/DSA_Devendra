class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            v1 = best + nums[i]
            v2 = nums[i]
            best = max(v1,v2)
            ans = max(ans,best)
        return ans