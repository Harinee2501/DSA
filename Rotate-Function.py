1class Solution(object):
2    def maxRotateFunction(self, nums):
3        ''' logic used
4        if array used is [a,b,c,d], so i from 1 to n-1 we should find 0a+1b+2c+3d 
5        and next step it goes 1a+2b+3c+4d so every step i increases except for the last element whose i becomes 0 meaning it wont come in next func computation, so after first computation F(0) we add that with the sum so i+1 so next F(1) and to remove last index contribution we subtract that from new F
6        '''
7        total=sum(nums)
8        n=len(nums)
9        F=0
10        for i in range(n):
11            F+=(i*nums[i])
12        ans=F
13        for i in range(1,n):
14            F=F+total-(n*nums[n-i])
15            ans=max(ans,F)
16        return ans