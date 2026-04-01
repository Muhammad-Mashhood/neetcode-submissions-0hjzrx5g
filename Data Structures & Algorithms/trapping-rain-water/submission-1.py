class Solution:
    def trap(self, height: list[int]) -> int:
        if not height: return 0
        
        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        total = 0
        h=height
        while l < r:
            if leftmax<rightmax:
                l+=1
                leftmax=max(h[l],leftmax)
                total+=leftmax-h[l]
            else :
                r-=1
                rightmax=max(h[r],rightmax)
                total+=rightmax-h[r]

                
        return total