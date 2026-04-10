class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def memoization(i, cache):
            if i >= len(cost):
                return 0
            if i in cache:
                return cache[i]

            cache[i] = cost[i] + min(memoization(i + 1, cache), memoization(i + 2, cache))
            return cache[i]

        print(memoization(0, {}))
        print(memoization(1, {}))

        return min(memoization(0, {}), memoization(1, {}))