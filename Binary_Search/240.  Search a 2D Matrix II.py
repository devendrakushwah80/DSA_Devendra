class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        col=0
        row=n-1
        while row>=0 and col<m:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                row -=1
            else:
                col +=1
        return False
