class Solution(object):
    def minimumPushes(self, word):
        n=len(word)
        count=Counter(word)
        sorted_count=sorted(count.values(),reverse=True)
        ans=0
        for i in range(len(sorted_count)):
            if i<=7:
                ans+=sorted_count[i]
            elif i<=15:
                ans+=sorted_count[i]*2
            elif i<=23:
                ans+=sorted_count[i]*3
            else:
                ans+=sorted_count[i]*4
        return ans