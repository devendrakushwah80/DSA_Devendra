class Solution:
    def reverseWords(self, s: str) -> str:
        s =  list(s.split())
        li =[]
        for i in s:
            i = list(i)
            l = 0
            h = len(i)-1
            while l<h:
                i[l],i[h]=i[h],i[l]
                l+=1
                h-=1
            li.append("".join(i))
        return " ".join(li)