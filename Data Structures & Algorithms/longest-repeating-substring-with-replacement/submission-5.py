class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            char = s[right]
            frequencies[char] = frequencies.get(char, 0) + 1 #counter increment
            
            maxFrequency = max(frequencies.values())

            while ((right - left + 1) - maxFrequency) > k:
                frequencies[s[left]] = frequencies[s[left]] - 1
                left += 1
            
            longest = max(longest, right + 1 - left) # the window

        return longest






        