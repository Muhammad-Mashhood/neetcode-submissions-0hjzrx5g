class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,v in enumerate(nums):
            c=target-v
            if c in seen:
                return [seen[c],i]
            seen[v]=i
        