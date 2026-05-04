1class Solution(object):
2    def rotate(self, matrix):
3        n=len(matrix)
4        for i in range(n):
5            for j in range(i+1,n):
6                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
7        for i in matrix:
8            i.reverse()
9        return matrix
10        