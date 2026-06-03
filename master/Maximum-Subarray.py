1class Solution(object):
2    def maxSubArray(self, nums):
3        ans=0
4        final=float('-inf')
5        for i in range(len(nums)):
6            ans+=nums[i]
7            final=max(ans,final) 
8            if ans<0:
9                ans=0
10        return final          