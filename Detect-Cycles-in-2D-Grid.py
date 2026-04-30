1class Solution(object):
2    def containsCycle(self, grid):
3        m=len(grid)
4        n=len(grid[0])
5        queue=deque([])
6        directions=[(0,1),(0,-1),(1,0),(-1,0)]
7        visited=set()
8        for i in range(m):
9            for j in range(n):
10                if (i,j) not in visited:
11                    start,end=i,j
12                    queue.append((i,j,-1,-1))
13                    visited.add((i,j))
14                    while queue:
15                        x,y,par_x,par_y=queue.popleft()
16                        for dx,dy in directions:
17                            new_x,new_y=x+dx,y+dy
18                            if 0<=new_x<m and 0<=new_y<n and grid[new_x][new_y]==grid[x][y]:
19                                if (new_x,new_y) not in visited:
20                                    queue.append((new_x,new_y,x,y))
21                                    visited.add((new_x,new_y))
22                                elif (new_x,new_y)!=(par_x,par_y):
23                                    return True
24        return False