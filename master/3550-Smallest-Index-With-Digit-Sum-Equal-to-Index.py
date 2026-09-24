class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            total=0
            while nums[i]>=10:
                total+=nums[i]%10
                nums[i]=nums[i]//10
            if nums[i]<10:
                total+=nums[i]            
            if total==i:
                return i
        return -1