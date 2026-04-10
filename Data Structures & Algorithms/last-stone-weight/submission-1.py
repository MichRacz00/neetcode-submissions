class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [s * -1 for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            newStone = heapq.heappop(stones) - heapq.heappop(stones)
            if newStone == 0:
                continue
            heapq.heappush(stones, newStone)
        
        res = -1 * heapq.heappop(stones) if len(stones) > 0 else 0
        return res
            
