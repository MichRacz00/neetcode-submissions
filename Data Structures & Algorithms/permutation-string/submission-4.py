class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freqs = [0]*26
        s2_freqs = [0]*26

        for char in s1:
            i = ord(char) - ord('a')
            s1_freqs[i] += 1

        l, r = -1 * len(s1), 0

        while r in range(len(s2)):
            if l >= 0:
                i_out = ord(s2[l]) - ord('a')
                s2_freqs[i_out] -= 1
            i_in = ord(s2[r]) - ord('a')
            s2_freqs[i_in] += 1

            if s1_freqs == s2_freqs:
                return True

            l, r = l + 1, r + 1
        
        return False