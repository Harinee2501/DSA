1class Solution(object):
2    def rotatedDigits(self, n):
3        # using prev solutions to find for progressing ones, so for less that 10 use the concept of valid dp[i]=2, invalid dp[i]=0, same dp[i]=1. and then use this for numbers greater than 10, like any number greater than 10 can be split into 2 parts by that numbers quotient and reminder so then using the dp values for those 2 numbers to decide for the current number
4        dp=[0]*(n+1)
5        count=0
6        for i in range(n+1):
7            if i<10:
8                if i in (3,4,7):
9                    dp[i]=0
10                elif i in (2,5,6,9):
11                    dp[i]=2
12                    count+=1
13                else:
14                    dp[i]=1
15            else:
16                a=dp[i//10]
17                b=dp[i%10]
18                if a==0 or b==0:
19                    dp[i]=0
20                elif a==1 and b==1:
21                    dp[i]=1
22                else:
23                    dp[i]=2
24                    count+=1
25        return count