1class Solution(object):
2    def countSubmatrices(self, grid, k):
3        m=len(grid)
4        n=len(grid[0])
5        ans=0
6        for i in range(m):
7            for j in range(n):
8                if i==0 and j==0:
9                    if grid[i][j]<=k:
10                        ans+=1
11                    continue
12                elif i==0:
13                    grid[i][j]+=grid[i][j-1]
14                elif j==0:
15                    grid[i][j]+=grid[i-1][j]
16                else:
17                    grid[i][j]+=grid[i-1][j]+grid[i][j-1]-grid[i-1][j-1]
18                if grid[i][j]<=k:
19                    ans+=1
20        print(grid)
21        return ans