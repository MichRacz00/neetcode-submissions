class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []

        for n in nums:
            heapq.heappush(maxHeap, -1 * n)

        res = 0
        for _ in range(k):
            res = heapq.heappop(maxHeap)
        return -1 * res