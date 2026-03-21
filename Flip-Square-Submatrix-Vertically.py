1class Solution(object):
2    def reverseSubmatrix(self, grid, x, y, k):
3        for i in range(y,y+k):
4            up=x
5            down=x+k-1
6            while up<down:
7                grid[up][i],grid[down][i]=grid[down][i],grid[up][i]
8                up+=1
9                down-=1
10        return grid