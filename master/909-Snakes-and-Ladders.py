class Solution(object):
    def snakesAndLadders(self, board):
        n=len(board)
        def pos(square):
            r=(square-1)//n
            c=(square-1)%n
            row=n-1-r
            if r%2==1:
                c=n-1-c
            return row,c
        target=n*n
        queue=deque([(1,0)])
        visited=set()
        visited.add(1)
        while queue:
            curr,rolls=queue.popleft()
            if curr==target:
                return rolls
            for i in range(curr+1,min(curr+6,target)+1):
                r,c=pos(i)
                if board[r][c]!=-1:
                    i=board[r][c]
                if i not in visited:
                    queue.append((i,rolls+1))
                    visited.add(i)
        return -1

