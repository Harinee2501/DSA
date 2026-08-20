class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        count=defaultdict(set)
        for i,j in reservedSeats:
            count[i].add(j)
        ans=(n-len(count))*2
        for i in count:
            left=all(x not in count[i] for x in [2,3,4,5])
            right=all(x not in count[i] for x in [6,7,8,9])
            mid=all(x not in count[i] for x in [4,5,6,7])
            if left and right:
                ans+=2
            elif left or right or mid:
                ans+=1
        return ans
