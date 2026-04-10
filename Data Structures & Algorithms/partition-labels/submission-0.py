class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freqs = {}
        for c in s:
            freqs[c] = 1 + freqs.get(c, 0)
        
        seen = set()
        count = 1
        res = []
        for c in s:
            if c not in seen:
                seen.add(c)
            freqs[c] -= 1

            if freqs[c] == 0:
                seen.remove(c)
            if len(seen) == 0:
                res.append(count)
                count = 0
            count += 1

        return res