class Solution(object):
    def smallestPalindrome(self, s):
        if len(s)==1:
            return s
        arr=[0]*len(s)
        count=Counter(s)
        sorted_count=sorted(count.items())
        print(sorted_count)
        first=0
        last=len(s)-1
        mid=""
        for i in sorted_count:
            freq=i[1]
            while freq>1:
                arr[first]=i[0]
                arr[last]=i[0]
                freq-=2
                first+=1
                last-=1
            if freq==1:
                mid=i[0]
        if mid:
            arr[first]=mid
        return "".join(arr)