1class Solution(object):
2    def threeSum(self, nums):
3        res=set()    
4        for i in range(len(nums)):
5            temp=set()
6            for j in range(i+1,len(nums)):
7                ans=-1*(nums[i]+nums[j])
8                if ans in temp:
9                    res.add(tuple(sorted([nums[i],nums[j],ans])))
10                temp.add(nums[j])
11        return list(res)