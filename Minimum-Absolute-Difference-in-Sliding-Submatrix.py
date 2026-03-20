1class Solution(object):
2    def minAbsDiff(self, grid, k):
3        m=len(grid)
4        n=len(grid[0])
5        ans=[[0 for _ in range(n-k+1)]for _ in range(m-k+1)]
6        for i in range(m-k+1):
7            for j in range(n-k+1):
8                v=sorted(set(grid[x][y] for x in range(i,i+k) for y in range(j,j+k)))
9                if len(v)<=1:
10                    ans[i][j]=0
11                else:
12                    ans[i][j]=min(v[k+1]-v[k] for k in range(len(v)-1))
13        return ans