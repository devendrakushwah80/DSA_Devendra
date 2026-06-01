class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        l = 0
        res = []
        Min = float('inf')
        for h in range(1, len(arr)):
            diff = arr[h] - arr[l]
            if diff < Min:
                Min = diff
                res = [[arr[l], arr[h]]]
            elif diff == Min:
                res.append([arr[l], arr[h]])
            l += 1
        return res