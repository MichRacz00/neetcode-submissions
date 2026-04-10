from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)} {s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # Read length
            while s[j] != ' ':
                j += 1
            length = int(s[i:j])
            j += 1  # skip the space
            res.append(s[j:j+length])
            i = j + length
        return res
