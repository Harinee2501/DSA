1class Solution(object):
2    def generate(self, numRows):
3        arr=[[1]]
4        for i in range(numRows-1):
5            new=[0]+arr[-1]+[0]
6            temp=[]
7            for j in range(len(new)-1):  
8                temp.append(new[j]+new[j+1])  
9            arr.append(temp) 
10        return arr  