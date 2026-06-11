class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        l = 0
        curr_cost = 0
        ans = 0

        for h in range(len(s)):

            curr_cost += abs(ord(s[h]) - ord(t[h]))

            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            ans = max(ans, h - l + 1)

        return ans