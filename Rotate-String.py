1class Solution(object):
2    def rotateString(self, s, goal):
3        n=len(s)
4        length=n
5        if s==goal:
6            return True
7        while n>0:
8            temp=""
9            for i in range(length):
10                temp+=s[(i+1)%length]
11            if temp==goal:
12                return True
13            s=temp
14            n-=1
15        return False