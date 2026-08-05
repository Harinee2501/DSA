class Solution(object):
    def maxArea(self, height):
        first=0
        last=len(height)-1
        area=0
        while first<=last:
            area=max(area,(last-first)*min(height[first],height[last]))
            if height[first]<height[last]:
                first+=1
            else:
                last-=1
        return area