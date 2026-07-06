class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                continue
            if stack[-1]==s[i]:
                stack.pop()
                continue
            stack.append(s[i])
        while stack:
            res.append(stack[-1])
            stack.pop()
        res.reverse()
        return "".join(res)