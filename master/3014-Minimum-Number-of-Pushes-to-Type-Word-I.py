class Solution(object):
    def minimumPushes(self, word):
        n=len(word)
        count=0
        for i in range(n):
            if i<=7:
                count+=1
            elif i<=15:
                count+=2
            elif i<=23:
                count+=3
            else:
                count+=4
        return count