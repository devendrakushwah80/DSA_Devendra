class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        h = int(math.sqrt(c))
        while l<=h:
            Sum = (l*l)+(h*h)
            if Sum==c:
                return True
            elif Sum>c:
                h-=1
            else:
                l+=1
        return False
