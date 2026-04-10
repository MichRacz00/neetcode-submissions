class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for n in nums:
            freqs[n] = 1 + freqs.get(n, 0)

        return sorted(freqs.keys(), key=lambda x: freqs[x], reverse=True)[:k]