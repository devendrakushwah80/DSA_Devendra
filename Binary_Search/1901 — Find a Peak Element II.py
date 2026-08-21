class Solution:
        def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
            n = len(mat)
            m = len(mat[0])

            l = 0
            h = m - 1

            while l <= h:

                mid = (l + h) // 2
                max_row = 0
                for i in range(n):
                    if mat[i][mid] > mat[max_row][mid]:
                        max_row = i

                left = mat[max_row][mid - 1] if mid - 1 >= 0 else -1
                right = mat[max_row][mid + 1] if mid + 1 < m else -1

                if mat[max_row][mid] > left and mat[max_row][mid] > right:
                    return [max_row, mid]
                
                elif left > mat[max_row][mid]:
                    h = mid - 1
                else:
                    l = mid + 1
