class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring_length = 0
        l, r = 0, 0
        seen_char = set()

        while r < len(s):
            print(r, l)
            candidate = s[r]

            while candidate in seen_char:
                seen_char.remove(s[l])
                l += 1
                    
            else:
                r += 1
                seen_char.add(candidate)
                window_size = r - l
                max_substring_length = max(window_size, max_substring_length)
        
        return max_substring_length