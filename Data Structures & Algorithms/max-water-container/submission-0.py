class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        final=0
        while l<r:
            water=min(heights[l],heights[r])*(r-l)
            if heights[l]<=heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            final=max(water,final)
        return final