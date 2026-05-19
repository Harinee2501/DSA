1class Solution(object):
2    def findMedianSortedArrays(self, nums1, nums2):
3        nums=nums1+nums2
4        nums.sort()
5        left=0
6        right=len(nums)-1
7        if len(nums)%2!=0:
8            return float(nums[len(nums)/2])
9        else:
10            return (nums[len(nums)/2]+nums[(len(nums)-1)/2])/2.0