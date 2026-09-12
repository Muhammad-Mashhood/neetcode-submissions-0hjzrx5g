class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen=defaultdict(int)
        for j in nums:
            seen[j]+=1
        max=[]
        for idx,val in seen.items():
            max.append([val,idx])
        max.sort()
        res=[]
        while len(res)<k:
            res.append(max.pop()[1])
        return res