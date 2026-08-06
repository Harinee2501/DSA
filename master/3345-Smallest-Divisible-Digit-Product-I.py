class Solution(object):
    def product(self,n):
        mul=1
        while n>0:
            mul*=(n%10)
            n=n//10
        return mul
    def smallestNumber(self, n, t):
        while True:
            if self.product(n)%t==0:
                return n
            n+=1
        