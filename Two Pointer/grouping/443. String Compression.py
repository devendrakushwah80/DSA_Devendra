class Solution:
    def compress(self, chars: List[str]) -> int:

        l = 0
        count = 0
        res = []

        for h in range(len(chars)):
            if chars[l] == chars[h]:
                count += 1
            else:
                res.append(chars[l])
                if count > 1:
                    for digit in str(count):
                        res.append(digit)
                l = h
                count = 1
        res.append(chars[l])
        if count > 1:
            for digit in str(count):
                res.append(digit)
        chars[:] = res
        return len(res)