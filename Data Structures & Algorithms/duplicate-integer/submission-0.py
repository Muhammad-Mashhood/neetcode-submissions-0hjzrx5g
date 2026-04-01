class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for i,val in enumerate(nums):
            if val in seen:
                return True
            else:
                seen[val]=i
            
        return False
