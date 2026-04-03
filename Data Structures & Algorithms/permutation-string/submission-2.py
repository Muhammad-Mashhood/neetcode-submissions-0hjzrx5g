from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        # 1. Create a frequency map for s1
        s1_counts = Counter(s1)
        # 2. Create a frequency map for the first 'window' of s2
        window_counts = Counter(s2[:n1])

        # 3. Check if the very first window is a match
        if s1_counts == window_counts:
            return True

        # 4. Slide the window across s2
        for i in range(n1, n2):
            # Add the new character (on the right)
            char_in = s2[i]
            window_counts[char_in] += 1
            
            # Remove the old character (on the left)
            char_out = s2[i - n1]
            if window_counts[char_out] == 1:
                del window_counts[char_out]
            else:
                window_counts[char_out] -= 1
            
            # Compare maps (this handles duplicates perfectly!)
            if s1_counts == window_counts:
                return True

        return False