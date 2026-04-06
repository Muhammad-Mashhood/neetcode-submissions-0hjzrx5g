from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack=deque()
        
        ends=[']','}',')']
        start=['[','{','(']
        
        for i in s:
            
            if i in start:
                stack.append(i)
            if not stack:
                return False
            if i in ends:
                
                si=start.index(stack.pop())
                ei=ends.index(i)
                if si!=ei:
                    return False
        if not stack:
            return True
        else:
            return False

                