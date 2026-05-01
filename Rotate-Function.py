1class Solution(object):
2    def maxRotateFunction(self, nums):
3        total=sum(nums)
4        n=len(nums)
5        F=0
6        for i in range(n):
7            F+=(i*nums[i])
8        ans=F
9        for i in range(1,n):
10            F=F+total-(n*nums[n-i])
11            ans=max(ans,F)
12        return ans