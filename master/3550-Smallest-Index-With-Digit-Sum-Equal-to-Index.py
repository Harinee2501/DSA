class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            total=0
            num=nums[i]
            while num>=10:
                total+=num%10
                num=num//10
            if num<10:
                total+=num           
            if total==i:
                return i
        return -1