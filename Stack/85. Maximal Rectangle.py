class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        def largestRectangleArea(heights):
            stack = []
            max_area = 0
        
            for i in range(len(heights) + 1):
                curr_height = 0 if i == len(heights) else heights[i]
                while stack and heights[stack[-1]] > curr_height:
                    h = heights[stack.pop()]
                    if not stack:
                        width = i
                    else:
                        width = i - stack[-1] - 1
                    max_area = max(max_area, h * width)
                stack.append(i)
            return max_area
            
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0
            max_area = max(max_area, largestRectangleArea(heights))
        return max_area