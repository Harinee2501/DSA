1class Solution(object):
2    def removeOuterParentheses(self, s):
3        stack=0
4        decomposed=""
5        for i in s:
6            if i=='(':
7                if stack>0:
8                    decomposed+=i
9                stack+=1
10            else:
11                stack-=1
12                if stack>0:
13                    decomposed+=i
14        return decomposed