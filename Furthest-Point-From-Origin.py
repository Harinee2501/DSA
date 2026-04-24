1class Solution(object):
2    def furthestDistanceFromOrigin(self, moves):
3        left=moves.count('L')
4        right=moves.count('R')
5        l=r=0
6        if left>right:
7            move='l'
8        else:
9            move='r'
10        for i in moves:
11            if i=='L':
12                l+=1
13            elif i=='R':
14                r+=1
15            else:
16                if move=='l':
17                    l+=1
18                else:
19                    r+=1
20        return abs(l-r)
21        