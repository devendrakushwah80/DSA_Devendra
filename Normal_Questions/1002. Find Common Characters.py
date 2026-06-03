class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        common = {}

        for ch in words[0]:
            if ch in common:
                common[ch] += 1
            else:
                common[ch] = 1

        for word in words[1:]:

            curr = {}

            for ch in word:
                if ch in curr:
                    curr[ch] += 1
                else:
                    curr[ch] = 1

            for ch in list(common.keys()):
                if ch in curr:
                    common[ch] = min(common[ch], curr[ch])
                else:
                    common[ch] = 0

        res = []

        for ch, cnt in common.items():
            for _ in range(cnt):
                res.append(ch)

        return res