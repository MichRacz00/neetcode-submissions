class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        content = {}
        max_len = 0

        l, r = 0, 0
        while r in range(len(s)):
            content[s[r]] = 1 + content.get(s[r], 0)
            most_freq_char = max(content, key=lambda x: content[x])
            window_size = r - l + 1

            if window_size - content[most_freq_char] <= k:
                max_len = max(window_size, max_len)
            else:
                content[s[l]] -= 1
                l += 1
            r += 1
        
        return max_len

