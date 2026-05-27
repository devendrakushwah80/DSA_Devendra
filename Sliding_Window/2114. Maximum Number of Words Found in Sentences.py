class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        Max = float('-inf')
        for i in sentences:
            l = i.split()
            leng = len(i.split())
            if leng>Max:
                Max = leng
        return Max