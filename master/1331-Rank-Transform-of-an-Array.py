class Solution(object):
    def arrayRankTransform(self, arr):
        sorted_arr=sorted(arr)
        rank=defaultdict(int)
        ranking=1
        for i in range(len(sorted_arr)):
            if sorted_arr[i] not in rank:
                rank[sorted_arr[i]]=ranking
                ranking+=1
        for i in range(len(arr)):
            arr[i]=rank[arr[i]]
        return arr