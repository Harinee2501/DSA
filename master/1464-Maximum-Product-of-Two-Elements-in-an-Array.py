class Solution(object):
    def maxProduct(self, nums):
        heap=[-num for num in nums]
        heapq.heapify(heap)
        first=-heapq.heappop(heap)
        second=-heapq.heappop(heap)
        return (first-1)*(second-1)