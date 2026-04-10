class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def memoization(i, cache):
            if i < 0:
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(memoization(i - 1, cache), nums[i] + memoization(i - 2, cache))
            
            print(i, cache)
            return cache[i]

        return memoization(len(nums) - 1, {})
            