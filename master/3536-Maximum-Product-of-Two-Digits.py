class Solution(object):
    def maxProduct(self, n):
        max1=max2=float('-inf')
        while n>0:
            i=n%10
            if i>max1:
                max2=max1
                max1=i
            elif i>max2:
                max2=i
            n=n//10
        return max1*max2