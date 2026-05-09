class Solution:
    def reverseVowels(self, s: str) -> str:
        i =0
        j = len(s)-1
        List = list(s)
        vol = ['a','e','i','o','u']
        while i<j:
            while i<j and List[i].lower() not in vol:
                i+=1
            while i<j and List[j].lower() not in vol:
                j-=1
            List[i],List[j] = List[j],List[i]
            i+=1
            j-=1
        return "".join(List)
