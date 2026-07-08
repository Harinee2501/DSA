class Solution(object):
    def majorityElement(self, nums):
        num1,count1=0,0
        num2,count2=0,0
        n=len(nums)
        arr=[]
        for i in range(n):
            if num1==nums[i]:
                count1+=1
            elif num2==nums[i]:
                count2+=1
            elif count1==0:
                num1=nums[i]
                count1=1
            elif count2==0:
                num2=nums[i]
                count2=1
            else:
                count1-=1
                count2-=1
        count1=nums.count(num1)
        count2=nums.count(num2)
        if count1>n//3:
            arr.append(num1)
        if count2>n//3 and num1!=num2:
            arr.append(num2)
        return arr