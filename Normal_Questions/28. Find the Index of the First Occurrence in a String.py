class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack = list(haystack)
        needle = list(needle)
        i = 0
        while i<len(haystack):
            if haystack[i] != needle[0]:
                i+=1
                continue
            if haystack[i:i+len(needle)]==needle:
                return i  
            i+=1
        return -1