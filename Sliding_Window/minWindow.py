class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for ch in t:
            freq[ch] = freq.get(ch, 0) + 1
        low = 0
        count = len(t)
        ans = ""
        mini = float('inf')
        for high in range(len(s)):
            if s[high] in freq:
                if freq[s[high]] > 0:
                    count -= 1
                freq[s[high]] -= 1
            while count == 0:
                if high - low + 1 < mini:
                    mini = high - low + 1
                    ans = s[low:high + 1]
                if s[low] in freq:
                    freq[s[low]] += 1
                    if freq[s[low]] > 0:
                        count += 1
                low += 1
        return ans