class Solution(object):
    def kClosest(self, points, k):
        heap=[]
        for x,y in points:
            distance=((x**2)+(y**2))**1/2
            heapq.heappush(heap,(distance,(x,y)))
        ans=[]
        for _ in range(k):
            ans.append(heapq.heappop(heap))
        return [i[1] for i in ans]