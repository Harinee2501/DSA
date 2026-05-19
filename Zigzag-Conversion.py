1class Solution(object):
2    def convert(self, s, numRows):
3        if numRows==1 or numRows>=len(s):
4            return s
5        ans=[""]*numRows
6        row=0
7        flag=False
8        for i in range(len(s)):
9            ans[row]+=s[i]
10            if row==0 or row==numRows-1:
11                flag=not flag
12            row+=1 if flag else -1
13        return "".join(ans)