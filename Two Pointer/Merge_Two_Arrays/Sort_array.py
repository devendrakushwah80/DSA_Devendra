class Solution:
    from typing import List

    def sortedSquares(self, nums: List[int]) -> List[int]:
        siz = len(nums)
        neg = []
        pos = []

        # Separate negatives and positives
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        # Case 1: No negative numbers
        if len(neg) == 0:
            return [x * x for x in pos]

        # Case 2: No positive numbers
        if len(pos) == 0:
            res = [x * x for x in neg]
            res.reverse()
            return res

        # Case 3: Both exist
        neg = [x * x for x in neg][::-1] #sq, reverse
        pos = [x * x for x in pos] #sq
        n, m = len(neg), len(pos)
        res = []
        #id

        i = j = 0
        #i=0
        #j=0
        while i < n and j < m:
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i += 1
                #i=i+1
            else:
                res.append(pos[j])
                j += 1
# while loop khartam

        while i < n:
            res.append(neg[i])
            i += 1

        while j < m:
            res.append(pos[j])
            j += 1

        return res