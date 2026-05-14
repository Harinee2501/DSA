1class Solution(object):
2    def isGood(self, nums):
3        num=max(nums)
4        n=len(nums)
5        if num!=n-1:
6            return False
7        count=Counter(nums)
8        for i in count:
9            if count[num]>2 or (count[i]>1 and i!=num):
10                return False
11        return True