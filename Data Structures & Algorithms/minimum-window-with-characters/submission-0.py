from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        # 1. Map what we NEED
        target_counts = Counter(t)
        need = len(target_counts)
        
        # 2. Track what we HAVE in current window
        window_counts = {}
        have = 0
        
        # Result tuple: (length, left_index, right_index)
        res, res_len = [-1, -1], float("inf")
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = 1 + window_counts.get(char, 0)
            
            # If this char is needed and we just hit the required count
            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1
            
            # 3. While the window is valid, try to shrink it
            while have == need:
                # Update our smallest window result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = (right - left + 1)
                
                # Pop the character from the left
                left_char = s[left]
                window_counts[left_char] -= 1
                
                # If removing this char makes the window invalid
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    have -= 1
                
                left += 1
        
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""