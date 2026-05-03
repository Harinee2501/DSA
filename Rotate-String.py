1class Solution(object):
2    def rotateString(self, s, goal):
3        if len(s)==len(goal) and goal in s+s:
4            return True
5        return False
6        # n=len(s)
7        # length=n
8        # if s==goal:
9        #     return True
10        # while n>0:
11        #     temp=""
12        #     for i in range(length):
13        #         temp+=s[(i+1)%length]
14        #     if temp==goal:
15        #         return True
16        #     s=temp
17        #     n-=1
18        # return False