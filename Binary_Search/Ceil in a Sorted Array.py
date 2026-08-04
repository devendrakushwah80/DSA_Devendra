class Solution:
    def findCeil(self, arr, x):
        l=0
        h=len(arr)-1
        res=-1
        while l<=h:
            m=(l+h)//2
            if arr[m]<x:
                l=m+1
            else:
                res = m
                h=m-1
        return res
