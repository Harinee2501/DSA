1class Solution(object):
2    def maxDistance(self, colors):
3        front=0
4        back=0
5        for i in range(len(colors)-1,0,-1):
6            if colors[i]!=colors[0]:
7                front=i
8                break
9        for i in range(len(colors)-1):
10            if colors[i]!=colors[-1]:
11                back=((len(colors)-1)-i)
12                break
13        return max(front,back)