class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        nums.sort()
        length = 0
        curLength = 1

        for i in range(1, len(nums)):
            print(nums[i - 1], nums[i])
            if nums[i - 1] == nums[i] - 1:
                curLength += 1
            elif nums[i - 1] == nums[i]:
                continue
            else:
                length = max(curLength, length)
                curLength = 1
        
        return max(curLength, length)