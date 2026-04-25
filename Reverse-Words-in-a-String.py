1class Solution(object):
2    def reverseWords(self, s):
3        new=""
4        b=s.split()
5        c=reversed(b)
6        new=" ".join(c)
7        return new
8