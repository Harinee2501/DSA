class Solution(object):
    def largestInteger(self, nums, k):
        n=len(nums)
        count=Counter(nums)
        if k==n:
            return max(nums)
        if k==1:
            ans=-1
            for i in nums:
                if count[i]==1:
                    ans=max(ans,i)
            return ans
        if count[nums[0]]==1 and count[nums[-1]]==1:
            return max(nums[0],nums[-1]) 
        elif count[nums[0]]==1:
            return nums[0]
        elif count[nums[-1]]==1:
            return nums[-1]
        else:
            return -1 