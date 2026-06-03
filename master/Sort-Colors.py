1class Solution(object):
2    def sortColors(self, nums):
3        
4        zero=nums.count(0)
5        one=nums.count(1)
6        two=nums.count(2)
7        for i in range(zero):
8            nums[i]=0
9        j=zero
10        for i in range(j,j+one):
11            nums[i]=1
12        k=zero+one
13        for i in range(k,k+two):
14            nums[i]=2
15        return nums