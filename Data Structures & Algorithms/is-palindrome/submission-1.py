import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stb=s.lower()
        st=re.sub('[^a-zA-z0-9]','',stb)
        length=len(st)
        for i in range(length):
            if st[i]!=st[length-i-1]:
                print(f"{st[i]},{st[length-i-1]}")
                return False
        return True
