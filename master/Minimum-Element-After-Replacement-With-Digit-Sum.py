1class Solution(object):
2    def minElement(self, nums):
3        ans=float('inf')
4        for i in range(len(nums)):
5            total=0
6            j=nums[i]
7            while j>=10:
8                total+=(j%10)
9                j=j//10
10            total+=j
11            nums[i]=total
12        return min(nums)
13            