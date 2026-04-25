1class Solution(object):
2    def removeOuterParentheses(self, s):
3        stack=[]
4        decomposed=""
5        for i in s:
6            if i=='(':
7                if len(stack)>0:
8                    decomposed+=i
9                stack.append(i)
10            else:
11                stack.pop()
12                if len(stack)>0:
13                    decomposed+=i
14        return decomposed