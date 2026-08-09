class Solution:
    def findKRotation(self, arr):
        l =0
        h = len(arr)-1
        while l<h:
            m = (l+h)//2
            if arr[m]>arr[h]:
                l=m+1
            else:
                h=m
        return l


# MY Brute Foce approach:
class Solution:
    def findKRotation(self, arr):
        c=0
        for i in range(len(arr)):
            if arr[i]>arr[len(arr)-1]:
                c+=1
        return c
