1class Solution(object):
2    def twoEditWords(self, queries, dictionary):
3        ans=[]
4        for i in queries:
5            for j in dictionary:
6                diff=0
7                for k in range(len(i)):
8                    if i[k]!=j[k]:
9                        diff+=1
10                    if diff>2:
11                        break
12                if diff<=2:
13                    ans.append(i)
14                    break
15        return ans