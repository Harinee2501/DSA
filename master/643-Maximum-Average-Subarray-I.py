class Solution(object):
    def findMaxAverage(self, nums, k):
        total=sum(nums[:k])
        avg=float(total)/k
        for i in range(k,len(nums)):
            total-=nums[i-k]
            total+=nums[i]
            avg=max(avg,float(total)/k)
        return avg