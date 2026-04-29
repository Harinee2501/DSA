1from collections import deque
2class Solution(object):
3    def solve(self, board):
4        m=len(board)
5        n=len(board[0])
6        queue=deque([])
7        for i in range(m):
8            if board[i][0]=="O":
9                queue.append((i,0))
10            if board[i][n-1]=="O":
11                queue.append((i,n-1))
12        for j in range(n):
13            if board[0][j]=="O":
14                queue.append((0,j))
15            if board[m-1][j]=="O":
16                queue.append((m-1,j))
17        directions=[(0,1),(1,0),(0,-1),(-1,0)]
18        while queue:
19            x,y=queue.popleft()
20            board[x][y]="T"
21            for dx,dy in directions:
22                new_x,new_y=x+dx,y+dy
23                if 0<=new_x<m and 0<=new_y<n and board[new_x][new_y]=="O":
24                    queue.append((new_x,new_y))
25                    board[new_x][new_y]="T"
26        for i in range(m):
27            for j in range(n):
28                if board[i][j]=="O":
29                    board[i][j]="X"
30                if board[i][j]=="T":
31                    board[i][j]="O"
32        return board