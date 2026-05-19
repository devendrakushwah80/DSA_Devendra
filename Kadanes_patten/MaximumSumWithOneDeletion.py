class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        noDel = arr[0]
        oneDel = float('-inf')
        res = arr[0]

        for i in range(1, len(arr)):
            prevNoDel = noDel

            noDel = max(arr[i], noDel + arr[i])

            oneDel = max(prevNoDel, oneDel + arr[i])

            res = max(res, noDel, oneDel)

        return res
