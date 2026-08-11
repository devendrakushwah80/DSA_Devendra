class Solution:
    def func(self, arr, n, speed):
        hours = 0
        for i in range(n):
            hours += arr[i] // speed
            if arr[i] % speed != 0:
                hours += 1
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        low = 1
        high = max(piles)
        res = high

        while low <= high: 
            guess = (low + high) // 2
            hour = self.func(piles, n, guess)
            if hour > h:
                low = guess + 1
            else:
                res = guess
                high = guess-1
        return res   
