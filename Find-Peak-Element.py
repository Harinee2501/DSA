1class Solution(object):
2    def findPeakElement(self, nums):
3        l=0
4        r=len(nums)-1
5        while l<r:
6            mid=(l+r)//2
7            if nums[mid]<nums[mid+1]:
8                l=mid+1
9            else:
10                r=mid
11        return l
12        