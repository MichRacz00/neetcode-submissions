class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.maxHeap = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, val)
        return heapq.nlargest(self.k, self.maxHeap)[-1]
        
