1class Solution(object):
2    def hasValidPath(self, grid):
3        m=len(grid)
4        n=len(grid[0])
5        print(m,n)
6        queue=deque([])
7        queue.append((0,0))
8        directions={1:[(0,-1),(0,1)],2:[(-1,0),(1,0)],3:[(0,-1),(1,0)],4:[(0,1),(1,0)],5:[(0,-1),(-1,0)],6:[(0,1),(-1,0)]}
9        while queue:
10            x,y=queue.popleft()
11            if x==m-1 and y==n-1:
12                return True
13            for dx,dy in directions[grid[x][y]]:
14                new_x,new_y=x+dx,y+dy
15                if 0<=new_x<m and 0<=new_y<n:
16                    if grid[new_x][new_y]!=0:
17                        if (-dx,-dy) in directions[grid[new_x][new_y]]:
18                            queue.append((new_x,new_y))
19                            grid[x][y]=0
20        return False