class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        h = len(height) - 1

        leftMax = 0
        rightMax = 0

        water = 0

        while l < h:

            if height[l] < height[h]:

                if height[l] >= leftMax:
                    leftMax = height[l]
                else:
                    water += leftMax - height[l]

                l += 1

            else:

                if height[h] >= rightMax:
                    rightMax = height[h]
                else:
                    water += rightMax - height[h]

                h -= 1

        return water