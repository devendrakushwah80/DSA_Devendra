class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        h = len(height)-1
        n = len(height)
        Max = float('-inf')
        area = 0
        while l<h:
            width = h - l
            length = min(height[l],height[h])
            area = length * width
            Max = max(Max, area)
            if height[l]<height[h]:
                l+=1
            else:
                h-=1
        return Max
