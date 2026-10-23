class Solution(object):
    def containsCycle(self, grid):
        m=len(grid)
        n=len(grid[0])  
        queue=deque([])   
        visited=set()
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    queue.append((i,j,-1,-1))
                    visited.add((i,j)) 
                    while queue:
                        x,y,px,py=queue.popleft()
                        for dx,dy in directions:
                            nx,ny=x+dx,y+dy
                            if not (0<=nx<m and 0<=ny<n):
                                continue
                            if grid[nx][ny]!=grid[x][y]:
                                continue
                            if (nx,ny) in visited:
                                if (nx,ny)!=(px,py):
                                    return True
                            else:
                                queue.append((nx,ny,x,y))
                                visited.add((nx,ny))
        return False