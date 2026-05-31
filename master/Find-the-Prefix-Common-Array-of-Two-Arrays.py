1class Solution(object):
2    def findThePrefixCommonArray(self, A, B):
3        n=len(A) 
4        count=[0]*n
5        ans=[0]*n
6        for i in range(n):
7            count[A[i]-1]+=1
8            count[B[i]-1]+=1
9            for j in count:
10                if j==2:
11                    ans[i]+=1
12        return ans