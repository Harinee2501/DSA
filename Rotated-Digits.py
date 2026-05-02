1class Solution(object):
2    def rotatedDigits(self, n):
3        count=0
4        for i in range(1,n+1):
5            flag=True
6            ins=0
7            for j in str(i):
8                if j in ('3','4','7'):
9                    flag=False
10                elif j in ('2','5','6','9'):
11                    ins+=1
12            if flag and ins>0:
13                count+=1
14        return count