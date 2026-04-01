import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stb=s.lower()
        st=re.sub('[^a-zA-z0-9]','',stb)
       
        return st==st[::-1]
