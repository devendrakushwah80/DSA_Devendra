class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def fun(matrix,n,m,guess):
            row = n-1
            col=0
            count =0
            while row>=0 and col<m:
                if matrix[row][col]<=guess:
                    count+= row+1
                    col+=1
                else:
                    row-=1
            return count


        n=len(matrix)
        m=len(matrix[0])
        low = matrix[0][0]
        high = matrix[n-1][m-1]
        res = -1

        while low<=high:
            guess = (low+ high)//2
            ans = fun(matrix,n,m,guess)
            if ans<k:
                low = guess +1
            else :
                res = guess
                high = guess -1
        return res
