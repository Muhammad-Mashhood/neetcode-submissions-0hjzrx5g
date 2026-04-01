class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a string of only lowercase alphanumeric characters
        filtered_chars = "".join(char.lower() for char in s if char.isalnum())
        
        # Compare the string to its reverse
        return filtered_chars == filtered_chars[::-1]