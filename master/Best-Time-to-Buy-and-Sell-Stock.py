1class Solution(object):
2    def maxProfit(self, prices):
3        left=0
4        right=1
5        sale=0
6        while right<len(prices):
7            if prices[left]>prices[right]:
8                left=right
9            else:
10                sale=max(prices[right]-prices[left],sale)
11            right+=1
12        return sale
13            