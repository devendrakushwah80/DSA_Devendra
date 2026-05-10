class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        maxFreq = 0
        res = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            maxFreq = max(maxFreq, freq[s[right]])

            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res