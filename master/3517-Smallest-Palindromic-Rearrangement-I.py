class Solution(object):
    def smallestPalindrome(self, s):
        if len(s)==1:
            return s
        arr=[0]*len(s)
        count=Counter(s)
        first=0
        last=len(s)-1
        mid=""
        for i in 'abcdefghijklmnopqrstuvwxyz':
            pairs=count[i]//2
            for _ in range(pairs):
                arr[first]=i
                arr[last]=i
                first+=1
                last-=1
            if count[i]%2:
                mid=i
        if mid:
            arr[first]=mid
        return "".join(arr)