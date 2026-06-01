1class Solution(object):
2    def minimumCost(self, cost):
3        if len(cost)<=2:
4            return sum(cost)
5        cost.sort(reverse=True)
6        left=0
7        ans=0
8        while left<len(cost):
9            if left==len(cost)-1:
10                ans+=cost[left]
11            else:
12                ans+=(cost[left]+cost[left+1])
13            left+=3
14        return ans