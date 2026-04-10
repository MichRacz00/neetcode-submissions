class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}
        for t in tasks:
            freqs[t] = freqs.get(t, 0) + 1

        maxHeap = [-1 * n for n in freqs.values()]
        heapq.heapify(maxHeap)
        
        q = deque([])
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                task = 1 + heapq.heappop(maxHeap)
                if task < 0:
                    q.append((task, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time