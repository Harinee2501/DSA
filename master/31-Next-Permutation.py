class Solution(object):
    def nextPermutation(self, nums): 
        n=len(nums)
        j=n-1
        diff=float('inf')
        while j>0:
            if nums[j]>nums[j-1]:
                for i in range(j,n):
                    sub=nums[i]-nums[j-1]
                    if sub>0 and sub<diff:
                        val=i
                        diff=sub
                nums[j-1],nums[val]=nums[val],nums[j-1]
                break
            j-=1
        nums[j:]=sorted(nums[j:])
        return nums