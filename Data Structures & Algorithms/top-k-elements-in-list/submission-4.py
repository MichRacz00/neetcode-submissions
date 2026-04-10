class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for n in nums:
            if n not in freqs.keys():
                freqs[n] = 1
            else:
                freqs[n] += 1

        sorted_freqs = [[] for _ in range(len(nums) + 1)]

        for key in freqs:
            sorted_freqs[freqs[key]].append(key)

        print(sorted_freqs)

        max_k = []
        for i in range(len(nums), -1, -1):
            if sorted_freqs[i] == []:
                continue

            if k <= 0:
                return max_k
            else:
                max_k.extend(sorted_freqs[i])
                k = k - len(sorted_freqs[i])
        
        return max_k
        