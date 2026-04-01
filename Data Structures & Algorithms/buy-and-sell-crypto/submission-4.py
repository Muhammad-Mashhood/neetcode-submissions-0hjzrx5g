class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l,r=0,1
        p=prices
        total=0
        
        while r<len(p):
            if p[l]<p[r]:
                total=max(total,p[r]-p[l])
                
            else:
                l=r
            r+=1

        return total