class Solution:
    def isPalindrome(self, s: str) -> bool:
        existing_string = ""
        
        s.strip().lower()
        for char in s:
            if char.isalnum():
                existing_string += char.lower()

        if existing_string[::-1] == existing_string:
            return True
        return False
        