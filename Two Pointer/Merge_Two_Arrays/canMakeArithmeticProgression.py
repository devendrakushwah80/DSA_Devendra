class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        i =0
        j = 1
        diff = arr[1]-arr[0]
        while j <len(arr):
            d = arr[j]-arr[i]
            if d == diff:
                i+=1
                j+=1
            else:
                return False
        return True
