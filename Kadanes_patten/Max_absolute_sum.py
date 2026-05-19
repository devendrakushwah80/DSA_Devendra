class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_end = 0
        max_sum = float('-inf')
        min_end = 0
        min_sum = float('inf')
        for X in nums:
            max_end = max(X,max_end+X)
            max_sum = max(max_sum,max_end)
            
            min_end = min(X,min_end+X)
            min_sum = min(min_sum,min_end)

        return max(abs(max_sum),abs(min_sum))