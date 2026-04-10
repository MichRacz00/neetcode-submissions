class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return max(nums)

        numsFirst, numsLast = nums.copy(), nums.copy()

        def memoization(i, stop, cache):
            if i > stop:
                return 0
            if i in cache:
                return cache[i]

            print(i)
            
            cache[i] = max(memoization(i + 1, stop, cache), nums[i] + memoization(i + 2, stop, cache))
            return cache[i]

        return max(memoization(0, len(nums) - 2, {}), memoization(1, len(nums) - 1, {}))