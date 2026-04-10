class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            i = (l + r) // 2

            if nums[i] < nums[r]:
                r = i
            else:
                l = i + 1
        return nums[l]