1class Solution(object):
2    def reversePairs(self, nums):
3        cnt=[0]
4        def mergeSort(nums,l,r):
5            if l>=r:
6                return 0
7            mid=(l+r)//2
8            mergeSort(nums,l,mid)
9            mergeSort(nums,mid+1,r)
10            j=mid+1
11            for i in range(l,mid+1):
12                while j<=r and nums[i]>(2*nums[j]):
13                    j+=1
14                cnt[0]+=j-(mid+1)
15            merge(nums,l,mid,r)
16        def merge(nums,l,mid,r):
17            temp=[]
18            p1=l
19            p2=mid+1
20            while p1<=mid and p2<=r:
21                if nums[p1]>nums[p2]:
22                    temp.append(nums[p2])
23                    p2+=1
24                else:
25                    temp.append(nums[p1])
26                    p1+=1
27            while p1<=mid:
28                temp.append(nums[p1])
29                p1+=1
30            while p2<=r:
31                temp.append(nums[p2])
32                p2+=1
33            for i in range(len(temp)):
34                nums[l+i]=temp[i]
35        mergeSort(nums,0,len(nums)-1)
36        return cnt[0]