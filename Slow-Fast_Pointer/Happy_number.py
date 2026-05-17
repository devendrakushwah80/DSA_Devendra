class Solution:
    def fun(self,n:int):
        sum = 0
        while n>0:
            d = n%10
            n = n//10
            sum += d*d
        return sum
    def isHappy(self, n: int) -> bool:

        slow = n
        fast = n
        while fast!=1:
            slow = self.fun(slow)
            fast = self.fun(fast)
            fast = self.fun(fast)
            if fast ==slow and slow!=1 :
                return False
        return True

