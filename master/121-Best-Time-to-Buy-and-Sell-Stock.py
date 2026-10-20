class Solution(object):
    def maxProfit(self, prices):
        #TC: O(n)
        #SC: O(1)
        profit=0
        i=0
        for j in range(1,len(prices)):
            if prices[j]-prices[i]<0:
                i=j
            else:
                profit=max(profit,prices[j]-prices[i])    
        return profit     