class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_substring_length = 0
        freqs = {}

        while r < len(s):
            freqs[s[r]] = 1 + freqs.get(s[r], 0)

            most_freq_char = max(freqs, key=freqs.get)
            remaining_chars = sum(freqs.values()) - freqs[most_freq_char]

            if remaining_chars > k:
                freqs[s[l]] -= 1
                l += 1
            else:
                max_substring_length = max(r - l + 1, max_substring_length)
            
            r += 1

        return max_substring_length