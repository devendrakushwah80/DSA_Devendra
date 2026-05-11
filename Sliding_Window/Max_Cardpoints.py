class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = 0
        rsum = 0
        maxsum = 0
        n = len(cardPoints)
        for i in range(k):
            lsum += cardPoints[i]
        maxsum = lsum
        rindex = n - 1
        for i in range(k - 1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rindex]
            rindex -= 1
            maxsum = max(maxsum, lsum + rsum)
        return maxsum