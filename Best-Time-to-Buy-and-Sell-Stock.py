1class Solution(object):
2    def maxProfit(self, prices):   
3        s1=0
4        s2=1
5        maxi=0
6        while s2<len(prices):
7            if prices[s2]-prices[s1]<=0:
8                s1=s2
9            else:
10                maxi=max(prices[s2]-prices[s1],maxi)
11            s2+=1
12        return maxi