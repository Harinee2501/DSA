1class Solution(object):
2    def rotateTheBox(self, boxGrid):
3        n=len(boxGrid)
4        m=len(boxGrid[0])
5        print(n,m)
6        ans=[[0 for _ in range(n)]for _ in range(m)]
7        for i in range(n):
8            for j in range(m):
9                ans[j][n-1-i]=boxGrid[i][j]
10        print(ans)
11        for j in range(n):
12            write=m-1
13            for i in range(m-1,-1,-1):
14                if ans[i][j]=='*':
15                    write=i-1
16                elif ans[i][j]=='#':
17                    ans[i][j]='.'
18                    ans[write][j]='#'
19                    write-=1
20        return ans