class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        freq = {}
        res = 0

        for high in range(len(s)):
            freq[s[high]] = freq.get(s[high], 0) + 1

            while freq[s[high]] > 1:
                freq[s[low]] -= 1
                low += 1

            res = max(res, high - low + 1)

        return res