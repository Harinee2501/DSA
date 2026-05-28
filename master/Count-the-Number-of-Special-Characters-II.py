1class Solution(object):
2    def numberOfSpecialChars(self, word):
3        upper=defaultdict(int)
4        lower=defaultdict(int)
5        count=0
6        for i in range(len(word)):
7            if word[i].isupper() and word[i] not in upper:
8                upper[word[i]]=i
9            else:
10                lower[word[i]]=i
11        for i in lower:
12            up=chr(ord(i)-32)
13            if up in upper:
14                if upper[up]>lower[i]:
15                    count+=1
16        return count