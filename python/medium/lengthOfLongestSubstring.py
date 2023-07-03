# This program takes a string s and finds the length of the longest
# substring within it that does not have repeating characters
# Rating: Medium
# Performance: Runtime O(N) -> beats ~90%

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r
        
        return length