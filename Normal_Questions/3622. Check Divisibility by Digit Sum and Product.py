class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = str(n)
        Sum = 0
        prod = 1
        for i in s:
            Sum += int(i)
            prod *= int(i)
        if (n%(Sum+prod))==0:
            return True
        else:
            return False
