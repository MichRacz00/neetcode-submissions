class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        
        nums = sorted(nums)
        seq, longest = 0, 0

        print(nums)

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]

            if diff == 1:
                seq += 1
            elif diff > 1:
                longest = max(seq, longest)
                seq = 0
        
        return max(seq, longest) + 1