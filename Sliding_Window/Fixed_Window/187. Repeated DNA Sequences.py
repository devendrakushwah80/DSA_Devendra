class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        ans = set()
        l = 0
        h = 9

        while h < len(s):
            substring = s[l:h+1]
            if substring in seen:
                ans.add(substring)
            else:
                seen.add(substring)
            l += 1
            h += 1

        return list(ans)