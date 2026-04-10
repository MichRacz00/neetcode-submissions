class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenChars = set()
        l, r = 0, 0

        maxLen = 0

        while r <= len(s) - 1:
            while s[r] in seenChars:
                seenChars.remove(s[l])
                l += 1
            
            seenChars.add(s[r])
            r += 1
            
            maxLen = max(maxLen, len(seenChars))
        
        return maxLen