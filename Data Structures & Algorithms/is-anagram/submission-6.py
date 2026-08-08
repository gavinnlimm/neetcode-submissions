class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = sorted(t)
        if sorted(s) == d:
            return True
        return False
