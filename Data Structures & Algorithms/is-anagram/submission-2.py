class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen=[]
        for v in s:
            seen+=v
        for v in t:
            if v not in seen:
                return False
            seen.remove(v)
        return True