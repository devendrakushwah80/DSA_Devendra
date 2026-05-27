class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = ""
        for i  in range(len(word)):
            if word[i]==ch:
                rev = word[:i+1]
                orr = word[i+1:]
                rev = rev[::-1]
                return rev+orr
        return word