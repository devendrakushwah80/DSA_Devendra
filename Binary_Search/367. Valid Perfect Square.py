class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        h = num
        while l<=h:
            mid=(l+h)//2
            if mid*mid==num:
                return True
            elif mid*mid<num:
                l=mid+1
            else:
                h=mid-1
        return False
