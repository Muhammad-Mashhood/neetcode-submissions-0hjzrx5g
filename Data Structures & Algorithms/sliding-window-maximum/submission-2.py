class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        maxa=[]
        for i in range(n-k+1):
            maxa.append(max(nums[i:i+k]))
        return maxa
