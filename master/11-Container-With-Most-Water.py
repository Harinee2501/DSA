class Solution(object):
    def maxArea(self, height):
        area=0
        first=0
        last=len(height)-1
        while first<=last:
            area=max(area,(last-first)*min(height[last],height[first]))
            if height[first]<height[last]:
                first+=1
            else:
                last-=1
        return area